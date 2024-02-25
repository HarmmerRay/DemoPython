# 导入包
import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 创建map对象
map = Map()
# 获取河南省疫情数据列表
f = open("疫情.txt", "r", encoding="utf-8")
data = f.read()
f.close()

data_dict = json.loads(data)
henan_data_list = data_dict["areaTree"][0]["children"][3]["children"]

henan_map_data = []
for data in henan_data_list:
    henan_map_data.append((data["name"] + "市", data["total"]["confirm"]))
print(henan_map_data)
map.add("河南省各地区疫情总确诊人数分布图", henan_map_data, "河南")
# 设置全局选项
map.set_global_opts(visualmap_opts=VisualMapOpts(
    is_show=True,
    is_piecewise=True,
    pieces=[
        {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
        {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
        {"min": 100, "max": 499, "label": "100-499人", "color": "#FF9966"},
        {"min": 500, "max": 999, "label": "500-999人", "color": "#FF6666"},
        {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
        {"min": 10000, "label": "10000人以上", "color": "#990033"}
    ]
))
# 绘图
map.render("henan_covid19_map.html")
