import requests
import xlwt
from bs4 import BeautifulSoup
import re
import openpyxl

datas = []
page = 0
while page <= 225:
    # 1、爬取数据
    url = f'https://movie.douban.com/top250?start={page}&filter='
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    movies = soup.find_all("div", class_="item")
    for movie in movies:
        data = []
        play_link = str(movie.find("a")["href"])
        data.append(play_link)
        poster = str(movie.find("img")["src"])
        data.append(poster)
        title = movie.find("span", class_="title").text
        data.append(title)
        info = movie.find("div", class_="bd").find("p").text.strip()
        info = re.compile(r'''[\u4e00-\u9fa5\d]+''').findall(info)

        start = info.index('导演')
        try:
            end = info.index('主演')
        except ValueError:
            try:end = info.index('主')
            except ValueError:
                end = info.index(str(re.compile(r'''\d+''').findall(info.__str__())[0]).strip("\n"))

        director = ""
        for name in range(start + 1, end):
            if name == end - 1:
                director = director + str(info[name])
                break
            director = director + str(info[name]) + "·"
        data.append(director)

        start = end
        date = str(re.compile(r'''\d+''').findall(info.__str__())[0]).strip("\n")
        end = info.index(date)

        main_actors = ""
        for name in range(start + 1, end):
            if name == end - 1:
                main_actors = main_actors + info[name]
                break
            main_actors = main_actors + info[name] + "、"
        data.append(main_actors)
        data.append(date)
        start = end
        type_words = [
            "动作", "喜剧", "剧情", "悬疑", "惊悚", "科幻", "奇幻", "恐怖",
            "爱情", "战争", "历史", "音乐", "西部", "青春", "家庭", "儿童",
            "体育", "传记", "冒险", "犯罪", "纪录片", "歌舞", "情色", "灾难",
            "黑色电影", "治愈系", "武侠", "军事", "校园", "励志", "侦探",
            "超级英雄", "动画", "网络", "实验", "独立", "短片", "长片", "默片",
            "同性"
        ]
        end += 2
        while True:
            try:
                type_words.index(info[end])
                break
            except ValueError:
                end += 1

        publish_country = ""
        for name in range(start + 1, end):
            if name == end - 1:
                publish_country += info[name]
                break
            publish_country += info[name] + "、"
        data.append(publish_country)

        start = end
        movie_type = ""
        end = len(info) - 1
        for name in range(start, end):
            if name == end - 1:
                movie_type += info[name]
                break
            movie_type += info[name] + "、"
        data.append(movie_type)

        start = end

        rating_rating_count = str(movie.find("div", class_="star").text).strip().split("\n\n")
        rating = rating_rating_count[0]
        data.append(rating)

        rating_count = rating_rating_count[1]
        data.append(rating_count)

        try:
            theme_point = movie.find("span", class_="inq").text
        except:
            theme_point = ""
        data.append(theme_point)
        # print(data)
        datas.append(data)
    page += 25


book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet("豆瓣电影TOP250", cell_overwrite_ok=True)
col = (
    '播放地址', '电影海报', '电影名称', '导演', '主演', '上映时间', '出品国家', '电影类型', '评分', '评价人数(人)',
    '灵魂动人点',
)
index = 0
for element in col:
    sheet.write(0, index, element)
    index += 1
row_num = 1
col_num = 0
for val in datas:
    for element in val:
        sheet.write(row_num, col_num, element)
        col_num += 1
    row_num += 1
    col_num = 0
book.save("./top250.xlsx")

workbook = openpyxl.load_workbook('./top250.xlsx')
worksheet = workbook.active
worksheet.column_dimension['A'].width = 30
for row in worksheet.iter_rows():
    row[0].row_height = 40
workbook.save('top250.xlsx')