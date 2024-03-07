import requests
import re

top250_list = []
start = 0
while start <= 225:
    # 1、爬取数据
    url = f'https://movie.douban.com/top250?start={start}&filter='
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}
    response = requests.get(url, headers=headers)
    data = response.text
    pattern = re.compile(r'<span class="title">(.+?)</span>')
    names = pattern.findall(data)
    print(names)
    # 2.提取数据
    for name in names:
        if name.startswith('&nbsp'):
            names.remove(name)
    start += 25
    for name in names:
        top250_list.append(name)
file = open("./top250.txt", "w", encoding="utf-8")
num = 1
for name in top250_list:
    file.write(str(num) + "." + name + "\r\n")
    num += 1
# print(top250_list)
