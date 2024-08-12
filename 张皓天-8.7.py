from pyecharts.charts import Bar
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10])
bar.render("基础柱状图.html")

from pyecharts.charts import Bar
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10])
bar.reversal_axis()
bar.render("基础柱状图.html")

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10], label_opts=LabelOpts(position="right"))
bar.reversal_axis()
bar.render("基础柱状图.html")

from pyecharts.charts import Bar,   Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
bar1=Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()
bar1.render("基础柱状图.html")


bar2=Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,50,50], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
bar2.render("基础柱状图.html")

bar3=Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[70,60,60], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()
bar3.render("基础柱状图.html")
timeline=Timeline({"theme":ThemeType.DARK})
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True)
timeline.render("基础时间线柱状图.html")





