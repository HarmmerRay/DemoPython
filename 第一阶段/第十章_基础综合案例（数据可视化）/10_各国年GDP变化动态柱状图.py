# 锻炼 力扇提博  数学 计算机 英语

from pyecharts.charts import Bar
from pyecharts.charts import Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

f = open("1960-2019全球GDP数据.csv", "r", encoding="GBK")
data_lines = f.readlines()
data_lines.pop(0)
# 读取数据并转化为 {"1999":[["中国","1111111"]]}这样的字典 列表 列表的数据格式
data_dict = {}
for line in data_lines:
    line_list = line.split(",")
    if data_dict.get(line_list[0]):
        data_dict.get(line_list[0]).append([line_list[1], line_list[2]])
    else:
        data_dict[line_list[0]] = [[line_list[1], line_list[2]]]
# 创建时间线并创建每一年的Bar加入到时间线中
# 设置时间线主题、数据顺序倒转、取前8个国家的数据、单位为亿、循环播放
timeline = Timeline(
    {"theme": ThemeType.DARK}
)
sorted(data_dict.keys())
for annual_gdp in data_dict:
    bar = Bar()
    x_list = []
    y_list = []
    for item in data_dict[annual_gdp]:
        item[1] = float(item[1])
    data_dict[annual_gdp].sort(key=lambda aa: aa[1], reverse=True)
    i = 0
    while i < 8:
        x_list.append(data_dict[annual_gdp][i][0])
        y_list.append(float(data_dict[annual_gdp][i][1]) / 100000000)
        i = i + 1
    x_list.reverse()
    y_list.reverse()
    bar.add_xaxis(x_list)
    bar.add_yaxis(annual_gdp + "年GDP(亿)", y_list, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(title_opts=TitleOpts(title=annual_gdp+"年全球前八GDP国家"))
    timeline.add(bar, annual_gdp)

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("各国年GDP变化动态柱状图.html")
# 一年对应一个bar
