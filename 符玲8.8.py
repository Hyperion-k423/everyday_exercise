# #8.8
#基础柱状图的开发
from pyecharts.charts import Bar#使用Bar构建基础柱状图
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])#添加x轴的数据
bar.add_yaxis("GDP",[30,20,10])#添加y轴数据
bar.render("基础柱状图.html")#绘图

#基础柱状图的开发
from pyecharts.charts import Bar#使用Bar构建基础柱状图
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])#添加x轴的数据
bar.add_yaxis("GDP",[30,20,10])#添加y轴数据
bar.reversal_axis()#反转x和y轴
bar.render("基础柱状图.html")#绘图

from pyecharts.charts import Bar#使用Bar构建基础柱状图
from pyecharts.options import LabelOpts
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])#添加x轴的数据
bar.add_yaxis("GDP",[30,20,10], label_opts=LabelOpts(position="right"))#添加y轴数据,labeil_opts部分添加数值标签在右侧显示
bar.reversal_axis()#反转x和y轴
bar.render("基础柱状图.html")#绘图


#演示带有时间线的柱状图开发
from pyecharts.charts import Bar,   Timeline#使用Bar构建基础柱状图
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
bar1=Bar()
bar1.add_xaxis(["中国","美国","英国"])#添加x轴的数据
bar1.add_yaxis("GDP",[30,20,10], label_opts=LabelOpts(position="right"))#添加y轴数据
bar1.reversal_axis()#反转x和y轴
bar1.render("基础柱状图.html")#绘图


bar2=Bar()
bar2.add_xaxis(["中国","美国","英国"])#添加x轴的数据
bar2.add_yaxis("GDP",[50,50,50], label_opts=LabelOpts(position="right"))#添加y轴数据
bar2.reversal_axis()#反转x和y轴
bar2.render("基础柱状图.html")#绘图

bar3=Bar()
bar3.add_xaxis(["中国","美国","英国"])#添加x轴的数据
bar3.add_yaxis("GDP",[70,60,60], label_opts=LabelOpts(position="right"))#添加y轴数据
bar3.reversal_axis()#反转x和y轴
bar3.render("基础柱状图.html")#绘图
timeline=Timeline({"theme":ThemeType.DARK})#构建时间线对象#设置主题
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")
timeline.add_schema(
    play_interval=1000,#自动播放的时间间隔，单位毫秒
    is_timeline_show=True,#是否在自动播放的时候，显示时间线
    is_auto_play=True,#是否自动播放
    is_loop_play=True)#是否循环播放
#绘图是用时间线对象绘图，而不是用bar对象了
timeline.render("基础时间线柱状图.html")






