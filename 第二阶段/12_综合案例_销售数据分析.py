from pyecharts.charts import Bar

# 读取数据，格式化
f = open("2011年1月销售数据.txt", "r", encoding="utf-8")
lines = f.readlines()
date_list = []
id_list = []
sale_volume_list = []
province_list = []
date_dict = {}
for line in lines:
    element = line.split(",")
    try:
        date_dict = {element[0]: date_dict[element[0]] + element[2]}


# 添加数据，设置选项
bar = Bar()
bar.add_xaxis(list(date_dict.values()))
bar.add_yaxis("销售额", list(date_dict.values()))
# 绘图
bar.render("销售额.html")
