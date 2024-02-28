from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts, InitOpts

# from pyecharts.globals import ThemeType
#
# # 读取数据，格式化
# f = open("2011年1月销售数据.txt", "r", encoding="utf-8")
# lines = f.readlines()
# date_list = []
# id_list = []
# sale_volume_list = []
# province_list = []
# date_dict = {}
# for line in lines:
#     element = line.split(",")
#     try:
#         date_dict[element[0]] = date_dict[element[0]] + float(element[2])
#     except KeyError:
#         date_dict[element[0]] = float(0)
#
# for key in date_dict:
#     print(key)
#     print(date_dict[key])
# # 添加数据，设置选项
# bar = Bar({"theme": ThemeType.DARK})
# bar.add_xaxis(list(date_dict.keys()))
# bar.add_yaxis("销售额", list(date_dict.values()))
#
# bar.set_global_opts()
# # 绘图
# bar.render("销售额.html")

# 面向对象思想设计程序
from data_record import Record
from file_define import CsvFileReader, JsonFileReader

# 1.FileReader  设计一个读取文件抽象类并用具体类实现
jan_data: list[Record] = CsvFileReader('2011年1月销售数据.txt').read_file()
feb_data: list[Record] = JsonFileReader('2011年2月销售数据JSON.txt').read_file()
all_data: list[Record] = jan_data + feb_data
# 2.DataCalculator
dict_date_money = {}
for data in all_data:
    try:
        dict_date_money[data.date] = float(dict_date_money[data.date]) + float(data.sale_volume)
        print(dict_date_money[data.date])
    except KeyError as e:
        dict_date_money[data.date] = data.sale_volume
print(dict_date_money)
# 3.Drawer
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(dict_date_money.keys()))
bar.add_yaxis("销售额", list(dict_date_money.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="全国每日总和销售额柱状图表"),

)
bar.render("销售额.html")
