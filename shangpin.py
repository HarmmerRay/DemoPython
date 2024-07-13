import json
import os

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

values = (1,2,3,4,5,6,7,8,9,10)
if not 2 > 3:
    print("yes")
