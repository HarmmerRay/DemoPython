import json
import os
import re
import subprocess
import traceback
from datetime import datetime, timedelta, time

import schedule

# with open('shangpin2.txt', 'r', encoding='utf-8') as file:
#     data = json.load(file)
# data = json.loads(data['result']['value'])
# num = 0
# for item in data['list']:
#     sumz = 0
#     print("item:",item)
#     print(num, end="  ")
#     num += 1
#     # print(item["sales"], end="  ")
#     if item.get('day30_volume_trend') is not None:
#         for i in item.get('day30_volume_trend'):
#             if i['volume'] is not None:
#                 sumz += int(i['volume'])
#     # 提取所需字段
#     product_info = {
#         "shangpin_id": item["promotion_id"],
#         "name": item["title"],
#         "url": "https://www.chanmama.com/promotionDetail/" + item["promotion_id"],
#         "industry": "",
#         "price": item["price"],
#         "yongjin": item["tb_max_commission_rate"],
#         "sale_amount": sumz,
#         "yesterday_sale_amount": "",
#         "daren_count": item["duration_author_count"],
#         "video_count": item["duration_video_count"],
#         "video_download": "",
#         "play_count": item["duration_aweme_volume"],
#         "zhuanhualv": item["duration_product_rate_text"],
#         "haopinlv": "",
#         "chanmama_fenlei": "",
#         "douyin_fenlei": "",
#         "pic": item["image"],
#         "douyin_url": item["dy_url"]
#     }
#     print(product_info)
#     print(sumz)

# for item in data['list']:
#     print(num, end="  ")
#     num += 1
#     print(item["duration_product_rate_text"])


# data = """{"result":{"type":"string","value":{"list":[{"name":"zy"},{"name":"zz"}]}}}"""
# data = json.loads(data)
# print(type(data))
# print(type(data['result']))
# print(type(data['result']['value']))
# print(type(data['result']['value']['list']))

# num = int("aaa")

# print(datetime.datetime.utcnow())
# expiry_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=1200)
# print(expiry_time)

# arr = []
# if not arr:
#     print("122222")

# def aaa():
#     video_list = []
#     author = {}
#     video_list = None
#     author = None
#     return video_list, author
#
#
# c = aaa()
# type(c)
# a, b = aaa()

# d = {'douyin_uid':"None"}
# if not d['douyin_uid']:
#     print("66666")
# print(len({}))
# print(len(None))


# if __name__ == '__main__':
#     # monitor_hot_videos()
#
#     # 计算最近的 3 小时的倍数时间点
#     now = datetime.now()
#     hours = now.hour
#     nearest_multiple_of_3 = round(hours / 3) * 3
#     if nearest_multiple_of_3 == 24:
#         nearest_multiple_of_3 = 0
#
#     nearest_time = now.replace(hour=nearest_multiple_of_3, minute=0, second=0, microsecond=0)
#
#     # 设置任务从最近的 3 小时的倍数时间点开始，并且每 3 小时执行一次
#     schedule.every(3).hours.at(f"{nearest_time.hour:02d}:00").do(monitor_hot_videos)
#
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# expires_at = "Fri, 25 Jul 2025 16:57:00 GMT"
# expires_at = datetime.datetime.strptime(expires_at, "%a, %d %b %Y %H:%M:%S %Z")
# rest_days = (expires_at - datetime.datetime.now()).days + 1
# print(rest_days)
# chajia  = (11599 - 4999) / 365
# print(rest_days * chajia)

# nearest_multiple_of_3 = int((int(datetime.now().hour / 3) + 1) * 3 % 24)
# nearest_time = time(hour=nearest_multiple_of_3, minute=0, second=0)
#
# # schedule.every(3).hours.at(f"{nearest_multiple_of_3:02d}:00").do(print)
# schedule.every(3).hours.at(nearest_time.strftime("%H:%M")).do(print)
#
# for job in schedule.jobs:
#     print(job.at_time.strftime("%H:%M:%S"))
# print()
# if '3' == 3:
#     print("666")
#
# data = """{"total_status": {"order_reminder": {"is_active": true, "frequency": 0}, "baokuan": {"is_active": true, "frequency": 0, "videoplay": 100, "zan": 1}, "review": {"is_active": true, "frequency": 0}, "accountDisconnected": {"is_active": true, "frequency": 0}, "zidongfabu": {"is_active": true, "frequency": 0}, "baiying": {"is_active": true, "frequency": 0}, "video": {"is_active": true, "frequency": 0}, "is_active": true}}"""
# data = json.loads(data)
# print(type(data))
# print(data['total_status'])
# choice = data['total_status']['zidongfabu']['frequency']
# print(type(choice))
# print(choice)

# now = datetime.now()
# nearest_multiple_of_3 = int((int(datetime.now().hour / 3) + 1) * 3 % 24)
# nearest_time =now.replace(hour=nearest_multiple_of_3, minute=0, second=0,microsecond=0)
# time_diff = (nearest_time - now).total_seconds()
# print(time_diff)

# try:
#     a = 1/0
# except Exception as e:
#     print("保持登录脚本异常"+str(e)+"\n异常栈:"+traceback.format_exc())
#     e = str(e)
#     print(type(e))
#     print(e)

# aaa = []
# if aaa:
#     print(11111)

# url = "https://www.iesdouyin.com/share/video/7395486171503004940/?region=CN&mid=7395486077290629899&u_code=-1&did=MS4wLjABAAAAF3x9s56NN88E13PbcoVVuq2e1uakUSt39ydRpjjlSac&iid=MS4wLjABAAAA9Ng3JMDlJOEkPefj5ABY-Hov1zLR09ZY_Cq1iC4HAHo&with_sec_did=1&titleType=title&share_sign=HFJjN42Ny8ap4zyUkxcOso2Br0z4At7ei84vXYBkORo-&share_version=290800&ts=1721986246&from_aid=1128&from_ssr=1"
# video_id = re.search(r'/(\d+)/', url).group(1)
# print(video_id)

# aaa = """b'{"errcode":0,"errmsg":"ok","msgid":3564882607550627844}'"""
# if "\"errcode\":0" in aaa:
#     print(5555555555)

# bbb = {"aaaa":555}
# if bbb['sss']:
#     print(11111)

# text = "Hello, 世界! 🇨🇳"
# # 尝试使用 GBK 编码将字符串编码为字节
# try:
#     encoded_text = text.encode('gbk')
# except UnicodeEncodeError as e:
#     print(f"编码错误: {e}")

# print(str({"code": -1, "msg": "获取cookie出错", "shangpins": []}))
# print(str("2312321"))

# aaa = "商品描述：AI副业，轻松赚外快"
# match = re.search(r'商品描述：(.*?)\n', aaa)
# if match:
#     short_title = match.group(1)
#     print(short_title)

# def xxx():
#     return 11,222
# a = xxx()
# print(type(a))
# if type(a) is tuple:
#     print(a[0],a[1])

aa = "111"
# json.dumps和str的不同
# title_clips方法的合成
# ts[1]不能为空的报错
# if aa == 1:
#     print("555")
# bb = {"title":"1111"}
# print(str(bb))
# visible_texture_id = "12321"
# touming_donghua_dict = {1: "sucai/mov/xiaoxinxin.mov", 2: "sucai/mov/saluozhuye.mov",
#                                 3: "sucai/mov/xinxinshandong.mov", 4: "", 5: "sucai/mov/luoye.mov", 6: "",
#                                 7: "", 8: "sucai/mov/xiayu.mov", 9: "", 10: "sucai/mov/huohua.mov",
#                                 11: "sucai/mov/yumaobengxian.mov", 12: "sucai/mov/mantianfanxing.mov",
#                                 13: "sucai/mov/xingxingfuxian.mov", 14: "sucai/mov/fenbanqingwu.mov",
#                                 15: "sucai/mov/qingbanxuanluo.mov", 16: "sucai/mov/baiyingguang.mov",
#                                 17: "sucai/mov/lvyingguang.mov"}
# touming_donghua = touming_donghua_dict.get(visible_texture_id)
# print(touming_donghua)
# def generate_video_inner_titles(shipin_title,shangpin_title,publish_type,template_properties):
#     # 两个title都是空的话，使用默认
#     if not (shipin_title or shangpin_title):
#         return {"title1": "强烈推荐", "title2": "超值！性价比高", 'title3': "网友：有这好东西，你不早告诉我"}
#
# print(generate_video_inner_titles(None,None,1,"333"))
# font_name = "SourceHanSansSC-Bold-2.otf"
# font_name = "usr/share/fonts/chinese/unifont.ttf"
# font_name = "wqy-zenhei.ttc"
# if os.path.exists(font_name):
#     print("目标字体存在")
#     # ffmpeg -i zimu.mp4 -vf "subtitles=zimu.mp4.srt:force_style='FontName=/usr/share/fonts/chinese/SourceHanSansSC-Bold-2.otf,FontSize=12,Alignment=2,MarginV=50,MarginL=20,MarginR=20'" -c:a copy zimu_output.mp4
#     command = f"""ffmpeg -i zimu.mp4 -vf "subtitles=zimu2.mp4.srt:force_style=\'FontName={font_name},FontSize=12,Alignment=2,MarginV=50,MarginL=20,MarginR=20\'" -c:a copy zimu_output.mp4"""
#     subprocess.call(command, shell=True)
# else:
#     print("目标字体不存在")

sss = 1 - 0.21314352
print(sss)