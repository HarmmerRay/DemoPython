from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "日本"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "日本"])
bar2.add_yaxis("GDP", [50, 40, 20], label_opts=LabelOpts(position="right"))

timeline = Timeline(
    {"theme": ThemeType.ROMA}
)
timeline.add(bar1, "2022年GDP")
timeline.add(bar2, "2023年GDP")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("时间线柱状图.html")
