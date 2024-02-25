import time

import requests

from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook

import pandas as pd
# 创建Excel文件
wb = Workbook()
ws = wb.active

# 爬取地址
url = f'https://www.maigoo.com/news/484526.html'
# 请求header
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/112.0.0.0 Safari/537.36'}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
tr_tags = soup.find('div', class_="md_1009 modelbox tcenter").get_text().split()
# tr_tags = soup.find_all('div', class_="md_1009 modelbox tcenter")
print(tr_tags)

time.sleep(0.01)
print(response)

# 将数据转换为DataFrame
df = pd.DataFrame(tr_tags[2:], columns=tr_tags[:2])  # 去除标题行

# 将DataFrame写入Excel文件
df.to_excel('output.xlsx', index=False)

# 将数据写入Excel表格中
# ws['A1'] = tr_tags[0]
# ws.column_dimensions['A'].width = 50  # 设置列宽为50个字符宽度

# 保存Excel文件
# wb.save('./output.xlsx')
