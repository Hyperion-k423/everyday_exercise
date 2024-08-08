from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
#1
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10])
bar.render("基础柱状图.html")
#2
bar1 = Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10])
bar1.reversal_axis()
bar1.render("基础柱状图1.html")
#3
bar2=Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDp",[30,20,10],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
bar2.render("基础柱状图2.html")
#4
bar3_1 = Bar()
bar3_1.add_xaxis(["中国","美国","英国"])
bar3_1.add_yaxis("GDp",[30,20,10],label_opts=LabelOpts(position="right"))
bar3_1.reversal_axis()
bar3_2 = Bar()
bar3_2.add_xaxis(["中国","美围","英国"])
bar3_2.add_yaxis("GDP",[50,30,20],label_opts=LabelOpts(position="right"))
bar3_2.reversal_axis()
timeline = Timeline()
timeline.add(bar3_1,"2021年GDP")
timeline.add(bar3_2,"2022年GDP")
timeline.render("基础柱状图-时间线.html")