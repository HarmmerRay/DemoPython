import socket

from selenium import webdriver
import time


# # 初始化 WebDriver
# driver = webdriver.Chrome()
#
# # 打开 Boss 直聘登录页面
# driver.get('https://www.zhipin.com/web/user/?ka=header-login')
#
# # 等待页面加载
# time.sleep(2)
#
# driver.quit()
# # 输入用户名和密码
# username = driver.find_element(By.XPATH, '//*[@id="loginUsername"]')
# password = driver.find_element(By.XPATH, '//*[@id="loginPassword"]')
#
# username.send_keys('你的用户名')
# password.send_keys('你的密码')
#
# # 点击登录按钮
# login_button = driver.find_element(By.XPATH, '//*[@id="submitBtn"]')
# login_button.click()
#
# # 等待登录成功
# time.sleep(5)
#
# # 打开消息页面
# driver.get('https://www.zhipin.com/chat/')
#
# # 等待消息页面加载
# time.sleep(5)
#
# # 找到第一个聊天对象并点击
# chat_list = driver.find_elements(By.CLASS_NAME, 'chat-item')
# if chat_list:
#     chat_list[0].click()
#     time.sleep(2)
#
# # 发送消息
# message_input = driver.find_element(By.CLASS_NAME, 'chat-input')
# message_input.send_keys('你好，我想了解一下贵公司的职位详情。')
# message_input.send_keys(Keys.RETURN)
#
# # 等待一段时间，确保消息发送成功
# time.sleep(2)
#
# # 关闭浏览器
# driver.quit()

# arrs = [1,23,4]
# for i in range(1,len(arrs)):
#     print(arrs[i])
#     i += 1


# for j in range(num_segments):
#     group_clips = []
#     change_index = []
#     i = 1
#     while i < len(groups_time[j]):
#         # todo 此处的逻辑会浪费很多短片段 比如groups_time[2.47,2.5,5.1,6.6] 添加到group_clips中就是[[2.47,2.5],[2.5,5.1]…… 因为插入第一个时间点的缘故
#         if abs(groups_time[j][i - 1] - groups_time[j][i]) >= 1.5:
#             group_clips.append(vf_video.subclip(groups_time[j][i - 1], groups_time[j][i]))
#             change_index.append(i - 1)
#             i += 1
#         else:
#             # 因为上面已经进行过1.5s阈值的片段合并，此处group_clips中只会有第一个片段比较短
#             group_clips.append(vf_video.subclip(groups_time[j][i - 1], groups_time[j][i + 1]))
#             change_index.append(i - 1)
#             i += 2
#         # print("chang_index", change_index)
#     print(f"clip_group {j + 1} 的变化索引：{change_index}")


# def get_local_ip_method1():
#     try:
#         # 创建一个 UDP 套接字
#         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         # 连接到一个外部地址（不发送数据，只是为了获取本地 IP 地址）
#         sock.connect(("8.8.8.8", 80))
#         local_ip = sock.getsockname()[0]
#         sock.close()
#         return local_ip
#     except Exception as e:
#         print(f"Error: {e}")
#         return None
# print(get_local_ip_method1())

print( int(7.89 * 10) / 10 )