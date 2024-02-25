import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts


# type是指0确诊 1治愈 2死亡 3新增确诊
def covid19_trend(filename_list, type) -> str:
    global type_name
    type = int(type)
    line = Line()
    for element in filename_list:
        file = open(element, "r", encoding="utf-8")
        data = file.read()
        # 剔除json数据前后的干扰数据
        begin = data.index("{")
        end = len(data) - data[::-1].index("}")
        data = data[begin:end:1]
        print(data)
        # json转化为字典
        data = json.loads(data)
        # 获取json中的相应数据，创建x y 轴
        trend_data = data['data'][type]['trend']
        print(trend_data)
        begin = list(trend_data['updateDate']).index("4.7")
        x_data = trend_data['updateDate'][begin:314:]
        y_data = trend_data['list'][type]['data'][begin:314:]
        print(x_data)
        print(y_data)
        type_name = trend_data['list'][type]['name']
        print(type_name)
        line.add_xaxis(x_data)
        line.add_yaxis(type_name, y_data)

    line.set_global_opts(
        title_opts=TitleOpts(title="每日" + type_name + "人数折线图"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
        visualmap_opts=VisualMapOpts(is_show=True)
    )
    return line.render("render.html")


if __name__ == '__main__':
    filename_list = ["印度.txt", "日本.txt", "美国.txt"]
    covid19_trend(filename_list, 0)
