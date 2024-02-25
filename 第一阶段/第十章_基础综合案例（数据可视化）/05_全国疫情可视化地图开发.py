# 导入包
import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 实例map
map = Map()
# 获得data
f = open("疫情.txt", "r", encoding="utf-8")
data = f.read()
f.close()
# json转换为所需的dict
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
# 拼装呈现图所需的数据
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
print(data_list)
# 添加数据
map.add("全国各地区确诊总人数分布图", data_list, "china")
# 设置全局设定
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
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
    )
)
# .render()输出
map.render("national_covid19_map.html")
