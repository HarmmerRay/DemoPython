import os
import threading
import time
import logging
import datetime

from pathlib import Path
import random
from urllib.parse import quote, urlencode

import yaml
from pydantic import BaseModel
from rich.logging import RichHandler
from logging.handlers import TimedRotatingFileHandler

import httpx
import json
import asyncio
import re
from httpx import Response

from encrypt.abogus import ABogus
from encrypt.msToken import MsToken


# 第一
class APIError(Exception):
    """基本API异常类，其他API异常都会继承这个类"""

    def __init__(self, status_code=None):
        self.status_code = status_code
        print(
            "程序出现异常，请检查错误信息。"
        )

    def display_error(self):
        """显示错误信息和状态码（如果有的话）"""
        return f"Error: {self.args[0]}." + (
            f" Status Code: {self.status_code}." if self.status_code else ""
        )


class APIConnectionError(APIError):
    """当与API的连接出现问题时抛出"""

    def display_error(self):
        return f"API Connection Error: {self.args[0]}."


class APIUnavailableError(APIError):
    """当API服务不可用时抛出，例如维护或超时"""

    def display_error(self):
        return f"API Unavailable Error: {self.args[0]}."


class APINotFoundError(APIError):
    """当API端点不存在时抛出"""

    def display_error(self):
        return f"API Not Found Error: {self.args[0]}."


class APIResponseError(APIError):
    """当API返回的响应与预期不符时抛出"""

    def display_error(self):
        return f"API Response Error: {self.args[0]}."


class APIRateLimitError(APIError):
    """当达到API的请求速率限制时抛出"""

    def display_error(self):
        return f"API Rate Limit Error: {self.args[0]}."


class APITimeoutError(APIError):
    """当API请求超时时抛出"""

    def display_error(self):
        return f"API Timeout Error: {self.args[0]}."


class APIUnauthorizedError(APIError):
    """当API请求由于授权失败而被拒绝时抛出"""

    def display_error(self):
        return f"API Unauthorized Error: {self.args[0]}."


class APIRetryExhaustedError(APIError):
    """当API请求重试次数用尽时抛出"""

    def display_error(self):
        return f"API Retry Exhausted Error: {self.args[0]}."


# 第二
class Singleton(type):
    _instances = {}  # 存储实例的字典
    _lock: threading.Lock = threading.Lock()  # 线程锁

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """
        重写默认的类实例化方法。当尝试创建类的一个新实例时，此方法将被调用。
        如果已经有一个与参数匹配的实例存在，则返回该实例；否则创建一个新实例。
        """
        key = (cls, args, frozenset(kwargs.items()))
        with cls._lock:
            if key not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[key] = instance
        return cls._instances[key]

    @classmethod
    def reset_instance(cls, *args, **kwargs):
        """
        重置指定参数的实例。这只是从 _instances 字典中删除实例的引用，
        并不真正删除该实例。如果其他地方仍引用该实例，它仍然存在且可用。
        """
        key = (cls, args, frozenset(kwargs.items()))
        with cls._lock:
            if key in cls._instances:
                del cls._instances[key]


class LogManager(metaclass=Singleton):
    def __init__(self):
        if getattr(self, "_initialized", False):  # 防止重复初始化
            return

        self.logger = logging.getLogger("Douyin_TikTok_Download_API_Crawlers")
        self.logger.setLevel(logging.INFO)
        self.log_dir = None
        self._initialized = True

    def setup_logging(self, level=logging.INFO, log_to_console=False, log_path=None):
        self.logger.handlers.clear()
        self.logger.setLevel(level)

        if log_to_console:
            ch = RichHandler(
                show_time=False,
                show_path=False,
                markup=True,
                keywords=(RichHandler.KEYWORDS or []) + ["STREAM"],
                rich_tracebacks=True,
            )
            ch.setFormatter(logging.Formatter("{message}", style="{", datefmt="[%X]"))
            self.logger.addHandler(ch)

        if log_path:
            self.log_dir = Path(log_path)
            self.ensure_log_dir_exists(self.log_dir)
            log_file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.log")
            log_file = self.log_dir.joinpath(log_file_name)
            fh = TimedRotatingFileHandler(
                log_file, when="midnight", interval=1, backupCount=99, encoding="utf-8"
            )
            fh.setFormatter(
                logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )
            )
            self.logger.addHandler(fh)

    @staticmethod
    def ensure_log_dir_exists(log_path: Path):
        log_path.mkdir(parents=True, exist_ok=True)

    def clean_logs(self, keep_last_n=10):
        """保留最近的n个日志文件并删除其他文件"""
        if not self.log_dir:
            return
        # self.shutdown()
        all_logs = sorted(self.log_dir.glob("*.log"))
        if keep_last_n == 0:
            files_to_delete = all_logs
        else:
            files_to_delete = all_logs[:-keep_last_n]
        for log_file in files_to_delete:
            try:
                log_file.unlink()
            except PermissionError:
                self.logger.warning(
                    f"无法删除日志文件 {log_file}, 它正被另一个进程使用"
                )

    def shutdown(self):
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)
        self.logger.handlers.clear()
        time.sleep(1)  # 确保文件被释放


def log_setup(log_to_console=True):
    logger = logging.getLogger("Douyin_TikTok_Download_API_Crawlers")
    if logger.hasHandlers():
        # logger已经被设置，不做任何操作
        return logger

    # 创建临时的日志目录
    temp_log_dir = Path("./logs")
    temp_log_dir.mkdir(exist_ok=True)

    # 初始化日志管理器
    log_manager = LogManager()
    log_manager.setup_logging(
        level=logging.INFO, log_to_console=log_to_console, log_path=temp_log_dir
    )

    # 只保留1000个日志文件
    log_manager.clean_logs(1000)

    return logger


logger = log_setup()


# 第三
class BaseCrawler:
    """
    基础爬虫客户端 (Base crawler client)
    """

    def __init__(
            self,
            proxies: dict = None,
            max_retries: int = 3,
            max_connections: int = 50,
            timeout: int = 10,
            max_tasks: int = 50,
            crawler_headers: dict = {},
    ):
        if isinstance(proxies, dict):
            self.proxies = proxies
            # [f"{k}://{v}" for k, v in proxies.items()]
        else:
            self.proxies = None

        # 爬虫请求头 / Crawler request header
        self.crawler_headers = crawler_headers or {}

        # 异步的任务数 / Number of asynchronous tasks
        self._max_tasks = max_tasks
        self.semaphore = asyncio.Semaphore(max_tasks)

        # 限制最大连接数 / Limit the maximum number of connections
        self._max_connections = max_connections
        self.limits = httpx.Limits(max_connections=max_connections)

        # 业务逻辑重试次数 / Business logic retry count
        self._max_retries = max_retries
        # 底层连接重试次数 / Underlying connection retry count
        self.atransport = httpx.AsyncHTTPTransport(retries=max_retries)

        # 超时等待时间 / Timeout waiting time
        self._timeout = timeout
        self.timeout = httpx.Timeout(timeout)
        # 异步客户端 / Asynchronous client
        self.aclient = httpx.AsyncClient(
            headers=self.crawler_headers,
            proxies=self.proxies,
            timeout=self.timeout,
            limits=self.limits,
            transport=self.atransport,
        )

    async def fetch_response(self, endpoint: str) -> Response:
        """获取数据 (Get data)

        Args:
            endpoint (str): 接口地址 (Endpoint URL)

        Returns:
            Response: 原始响应对象 (Raw response object)
        """
        return await self.get_fetch_data(endpoint)

    async def fetch_get_json(self, endpoint: str) -> dict:
        """获取 JSON 数据 (Get JSON data)

        Args:
            endpoint (str): 接口地址 (Endpoint URL)

        Returns:
            dict: 解析后的JSON数据 (Parsed JSON data)
        """
        response = await self.get_fetch_data(endpoint)
        return self.parse_json(response)

    async def fetch_post_json(self, endpoint: str, params: dict = {}, data=None) -> dict:
        """获取 JSON 数据 (Post JSON data)

        Args:
            endpoint (str): 接口地址 (Endpoint URL)

        Returns:
            dict: 解析后的JSON数据 (Parsed JSON data)
        """
        response = await self.post_fetch_data(endpoint, params, data)
        return self.parse_json(response)

    def parse_json(self, response: Response) -> dict:
        """解析JSON响应对象 (Parse JSON response object)

        Args:
            response (Response): 原始响应对象 (Raw response object)

        Returns:
            dict: 解析后的JSON数据 (Parsed JSON data)
        """
        if (
                response is not None
                and isinstance(response, Response)
                and response.status_code == 200
        ):
            try:
                return response.json()
            except json.JSONDecodeError as e:
                # 尝试使用正则表达式匹配response.text中的json数据
                match = re.search(r"\{.*\}", response.text)
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError as e:
                    logger.error("解析 {0} 接口 JSON 失败： {1}".format(response.url, e))
                    raise APIResponseError("解析JSON数据失败")

        else:
            if isinstance(response, Response):
                logger.error(
                    "获取数据失败。状态码: {0}".format(response.status_code)
                )
            else:
                logger.error("无效响应类型。响应类型: {0}".format(type(response)))

            raise APIResponseError("获取数据失败")

    async def get_fetch_data(self, url: str):
        """
        获取GET端点数据 (Get GET endpoint data)

        Args:
            url (str): 端点URL (Endpoint URL)

        Returns:
            response: 响应内容 (Response content)
        """
        for attempt in range(self._max_retries):
            try:
                response = await self.aclient.get(url, follow_redirects=True)
                if not response.text.strip() or not response.content:
                    error_message = "第 {0} 次响应内容为空, 状态码: {1}, URL:{2}".format(attempt + 1,
                                                                                         response.status_code,
                                                                                         response.url)

                    logger.warning(error_message)

                    if attempt == self._max_retries - 1:
                        raise APIRetryExhaustedError(
                            "获取端点数据失败, 次数达到上限"
                        )

                    await asyncio.sleep(self._timeout)
                    continue

                # logger.info("响应状态码: {0}".format(response.status_code))
                response.raise_for_status()
                return response

            except httpx.RequestError:
                raise APIConnectionError("连接端点失败，检查网络环境或代理：{0} 代理：{1} 类名：{2}"
                                         .format(url, self.proxies, self.__class__.__name__)
                                         )

            except httpx.HTTPStatusError as http_error:
                self.handle_http_status_error(http_error, url, attempt + 1)

            except APIError as e:
                e.display_error()

    async def post_fetch_data(self, url: str, params: dict = {}, data=None):
        """
        获取POST端点数据 (Get POST endpoint data)

        Args:
            url (str): 端点URL (Endpoint URL)
            params (dict): POST请求参数 (POST request parameters)

        Returns:
            response: 响应内容 (Response content)
        """
        for attempt in range(self._max_retries):
            try:
                response = await self.aclient.post(
                    url,
                    json=None if not params else dict(params),
                    data=None if not data else data,
                    follow_redirects=True
                )
                if not response.text.strip() or not response.content:
                    error_message = "第 {0} 次响应内容为空, 状态码: {1}, URL:{2}".format(attempt + 1,
                                                                                         response.status_code,
                                                                                         response.url)

                    logger.warning(error_message)

                    if attempt == self._max_retries - 1:
                        raise APIRetryExhaustedError(
                            "获取端点数据失败, 次数达到上限"
                        )

                    await asyncio.sleep(self._timeout)
                    continue

                # logger.info("响应状态码: {0}".format(response.status_code))
                response.raise_for_status()
                return response

            except httpx.RequestError:
                raise APIConnectionError(
                    "连接端点失败，检查网络环境或代理：{0} 代理：{1} 类名：{2}".format(url, self.proxies,
                                                                                   self.__class__.__name__)
                )

            except httpx.HTTPStatusError as http_error:
                self.handle_http_status_error(http_error, url, attempt + 1)

            except APIError as e:
                e.display_error()

    async def head_fetch_data(self, url: str):
        """
        获取HEAD端点数据 (Get HEAD endpoint data)

        Args:
            url (str): 端点URL (Endpoint URL)

        Returns:
            response: 响应内容 (Response content)
        """
        try:
            response = await self.aclient.head(url)
            # logger.info("响应状态码: {0}".format(response.status_code))
            response.raise_for_status()
            return response

        except httpx.RequestError:
            raise APIConnectionError("连接端点失败，检查网络环境或代理：{0} 代理：{1} 类名：{2}".format(
                url, self.proxies, self.__class__.__name__
            )
            )

        except httpx.HTTPStatusError as http_error:
            self.handle_http_status_error(http_error, url, 1)

        except APIError as e:
            e.display_error()

    def handle_http_status_error(self, http_error, url: str, attempt):
        """
        处理HTTP状态错误 (Handle HTTP status error)

        Args:
            http_error: HTTP状态错误 (HTTP status error)
            url: 端点URL (Endpoint URL)
            attempt: 尝试次数 (Number of attempts)
        Raises:
            APIConnectionError: 连接端点失败 (Failed to connect to endpoint)
            APIResponseError: 响应错误 (Response error)
            APIUnavailableError: 服务不可用 (Service unavailable)
            APINotFoundError: 端点不存在 (Endpoint does not exist)
            APITimeoutError: 连接超时 (Connection timeout)
            APIUnauthorizedError: 未授权 (Unauthorized)
            APIRateLimitError: 请求频率过高 (Request frequency is too high)
            APIRetryExhaustedError: 重试次数达到上限 (The number of retries has reached the upper limit)
        """
        response = getattr(http_error, "response", None)
        status_code = getattr(response, "status_code", None)

        if response is None or status_code is None:
            logger.error("HTTP状态错误: {0}, URL: {1}, 尝试次数: {2}".format(
                http_error, url, attempt
            )
            )
            raise APIResponseError(f"处理HTTP错误时遇到意外情况: {http_error}")

        if status_code == 302:
            pass
        elif status_code == 404:
            raise APINotFoundError(f"HTTP Status Code {status_code}")
        elif status_code == 503:
            raise APIUnavailableError(f"HTTP Status Code {status_code}")
        elif status_code == 408:
            raise APITimeoutError(f"HTTP Status Code {status_code}")
        elif status_code == 401:
            raise APIUnauthorizedError(f"HTTP Status Code {status_code}")
        elif status_code == 429:
            raise APIRateLimitError(f"HTTP Status Code {status_code}")
        else:
            logger.error("HTTP状态错误: {0}, URL: {1}, 尝试次数: {2}".format(
                status_code, url, attempt
            )
            )
            raise APIResponseError(f"HTTP状态错误: {status_code}")

    async def close(self):
        await self.aclient.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclient.aclose()


# 配置文件路径
path = os.path.abspath(os.path.dirname(__file__))

# 读取配置文件
with open(f"./config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)


# 第四

def gen_random_str(randomlength: int) -> str:
    """
    根据传入长度产生随机字符串 (Generate a random string based on the given length)

    Args:
        randomlength (int): 需要生成的随机字符串的长度 (The length of the random string to be generated)

    Returns:
        str: 生成的随机字符串 (The generated random string)
    """

    base_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-"
    return "".join(random.choice(base_str) for _ in range(randomlength))


def get_timestamp(unit: str = "milli"):
    """
    根据给定的单位获取当前时间 (Get the current time based on the given unit)

    Args:
        unit (str): 时间单位，可以是 "milli"、"sec"、"min" 等
            (The time unit, which can be "milli", "sec", "min", etc.)

    Returns:
        int: 根据给定单位的当前时间 (The current time based on the given unit)
    """

    now = datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)
    if unit == "milli":
        return int(now.total_seconds() * 1000)
    elif unit == "sec":
        return int(now.total_seconds())
    elif unit == "min":
        return int(now.total_seconds() / 60)
    else:
        raise ValueError("Unsupported time unit")


class TokenManager:
    douyin_manager = config.get("TokenManager").get("douyin")
    token_conf = douyin_manager.get("msToken", None)
    ttwid_conf = douyin_manager.get("ttwid", None)
    proxies_conf = douyin_manager.get("proxies", None)
    proxies = {
        "http://": proxies_conf.get("http", None),
        "https://": proxies_conf.get("https", None),
    }

    @classmethod
    def gen_real_msToken(cls) -> str:
        """
        生成真实的msToken,当出现错误时返回虚假的值
        (Generate a real msToken and return a false value when an error occurs)
        """

        payload = json.dumps(
            {
                "magic": cls.token_conf["magic"],
                "version": cls.token_conf["version"],
                "dataType": cls.token_conf["dataType"],
                "strData": cls.token_conf["strData"],
                "tspFromClient": get_timestamp(),
            }
        )
        headers = {
            "User-Agent": cls.token_conf["User-Agent"],
            "Content-Type": "application/json",
        }

        transport = httpx.HTTPTransport(retries=5)
        with httpx.Client(transport=transport, proxies=cls.proxies) as client:
            try:
                response = client.post(
                    cls.token_conf["url"], content=payload, headers=headers
                )
                response.raise_for_status()

                msToken = str(httpx.Cookies(response.cookies).get("msToken"))
                if len(msToken) not in [120, 128]:
                    raise APIResponseError("响应内容：{0}， Douyin msToken API 的响应内容不符合要求。".format(msToken))

                return msToken

            # except httpx.RequestError as exc:
            #     # 捕获所有与 httpx 请求相关的异常情况 (Captures all httpx request-related exceptions)
            #     raise APIConnectionError(
            #         "请求端点失败，请检查当前网络环境。 链接：{0}，代理：{1}，异常类名：{2}，异常详细信息：{3}"
            #         .format(cls.token_conf["url"], cls.proxies, cls.__name__, exc)
            #     )
            #
            # except httpx.HTTPStatusError as e:
            #     # 捕获 httpx 的状态代码错误 (captures specific status code errors from httpx)
            #     if e.response.status_code == 401:
            #         raise APIUnauthorizedError(
            #             "参数验证失败，请更新 Douyin_TikTok_Download_API 配置文件中的 {0}，以匹配 {1} 新规则"
            #             .format("msToken", "douyin")
            #         )
            #
            #     elif e.response.status_code == 404:
            #         raise APINotFoundError("{0} 无法找到API端点".format("msToken"))
            #     else:
            #         raise APIResponseError(
            #             "链接：{0}，状态码 {1}：{2} ".format(
            #                 e.response.url, e.response.status_code, e.response.text
            #             )
            #         )

            except Exception as e:
                # 返回虚假的msToken (Return a fake msToken)
                logger.error("请求Douyin msToken API时发生错误：{0}".format(e))
                logger.info("将使用本地生成的虚假msToken参数，以继续请求。")
                return cls.gen_false_msToken()

    @classmethod
    def gen_false_msToken(cls) -> str:
        """生成随机msToken (Generate random msToken)"""
        return gen_random_str(126) + "=="

    @classmethod
    def gen_ttwid(cls) -> str:
        """
        生成请求必带的ttwid
        (Generate the essential ttwid for requests)
        """

        transport = httpx.HTTPTransport(retries=5)
        with httpx.Client(transport=transport) as client:
            try:
                response = client.post(
                    cls.ttwid_conf["url"], content=cls.ttwid_conf["data"]
                )
                response.raise_for_status()

                ttwid = str(httpx.Cookies(response.cookies).get("ttwid"))
                return ttwid

            except httpx.RequestError as exc:
                # 捕获所有与 httpx 请求相关的异常情况 (Captures all httpx request-related exceptions)
                raise APIConnectionError(
                    "请求端点失败，请检查当前网络环境。 链接：{0}，代理：{1}，异常类名：{2}，异常详细信息：{3}"
                    .format(cls.ttwid_conf["url"], cls.proxies, cls.__name__, exc)
                )

            except httpx.HTTPStatusError as e:
                # 捕获 httpx 的状态代码错误 (captures specific status code errors from httpx)
                if e.response.status_code == 401:
                    raise APIUnauthorizedError(
                        "参数验证失败，请更新 Douyin_TikTok_Download_API 配置文件中的 {0}，以匹配 {1} 新规则"
                        .format("ttwid", "douyin")
                    )

                elif e.response.status_code == 404:
                    raise APINotFoundError("ttwid无法找到API端点")
                else:
                    raise APIResponseError("链接：{0}，状态码 {1}：{2} ".format(
                        e.response.url, e.response.status_code, e.response.text
                    )
                    )


class BaseRequestModel(BaseModel):
    device_platform: str = "webapp"
    aid: str = "6383"
    channel: str = "channel_pc_web"
    pc_client_type: int = 1
    version_code: str = "190500"
    version_name: str = "19.5.0"
    cookie_enabled: str = "true"
    screen_width: int = 1920
    screen_height: int = 1080
    browser_language: str = "zh-CN"
    browser_platform: str = "Win32"
    browser_name: str = "Firefox"
    browser_version: str = "124.0"
    browser_online: str = "true"
    engine_name: str = "Gecko"
    engine_version: str = "122.0.0.0"
    os_name: str = "Windows"
    os_version: str = "10"
    cpu_core_num: int = 12
    device_memory: int = 8
    platform: str = "PC"
    # webid: str = "7388296161008862738"
    # downlink: int = 10
    # effective_type: str = "4g"
    # round_trip_time: int = 100
    msToken: str = TokenManager.gen_real_msToken()


class PostDetail(BaseRequestModel):
    aweme_id: str


# 第五
class BogusManager:
    # 字典方法生成A-Bogus参数，感谢 @JoeanAmier 提供的纯Python版本算法。
    @classmethod
    def ab_model_2_endpoint(cls, params: dict, user_agent: str) -> str:
        if not isinstance(params, dict):
            raise TypeError("参数必须是字典类型")

        try:
            ab_value = ABogus().get_value(params, )
        except Exception as e:
            raise RuntimeError("生成A-Bogus失败: {0})".format(e))

        return quote(ab_value, safe='')


# 第第第
class DouyinWebCrawler:

    # 从配置文件中获取抖音的请求头
    async def get_douyin_headers(self):
        douyin_config = config["TokenManager"]["douyin"]
        kwargs = {
            "headers": {
                "Accept-Language": douyin_config["headers"]["Accept-Language"],
                "User-Agent": douyin_config["headers"]["User-Agent"],
                "Referer": douyin_config["headers"]["Referer"],
                "Cookie": douyin_config["headers"]["Cookie"],
            },
            "proxies": {"http://": douyin_config["proxies"]["http"], "https://": douyin_config["proxies"]["https"]},
        }
        return kwargs

    "-------------------------------------------------------handler接口列表-------------------------------------------------------"

    async def fetch_one_video(self, aweme_id: str):
        # 获取抖音的实时Cookie
        kwargs = await self.get_douyin_headers()
        # 创建一个基础爬虫
        base_crawler = BaseCrawler(proxies=kwargs["proxies"], crawler_headers=kwargs["headers"])
        async with base_crawler as crawler:
            # 创建一个作品详情的BaseModel参数
            params = PostDetail(aweme_id=aweme_id)
            # 生成一个作品详情的带有加密参数的Endpoint
            # 2024年6月12日22:41:44 由于XBogus加密已经失效，所以不再使用XBogus加密参数，转移至a_bogus加密参数。
            # endpoint = BogusManager.xb_model_2_endpoint(
            #     DouyinAPIEndpoints.POST_DETAIL, params.dict(), kwargs["headers"]["User-Agent"]
            # )

            # 生成一个作品详情的带有a_bogus加密参数的Endpoint
            params_dict = params.dict()
            msToken = MsToken()
            # params_dict["msToken"] = msToken.get_real_ms_token()
            params_dict["msToken"] = ""
            a_bogus = BogusManager.ab_model_2_endpoint(params_dict, kwargs["headers"]["User-Agent"])
            endpoint = f"https://www.douyin.com/aweme/v1/web/aweme/detail/?{urlencode(params_dict)}&a_bogus={a_bogus}"

            response = await crawler.fetch_get_json(endpoint)
        return response


async def get_videos(aweme_id: str):
    crawer = DouyinWebCrawler()
    aweme_id = "7376636271860518178"
    response = await crawer.fetch_one_video(aweme_id)
    print(response)
async def main():
    crawer = DouyinWebCrawler()
    aweme_id = "7376636271860518178"
    response = await crawer.fetch_one_video(aweme_id)
    print(response)
# asyncio.run(main())
