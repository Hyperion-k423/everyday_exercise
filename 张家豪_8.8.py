#第一个数据可视化案例
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = [("北京市",99),("上海市",199),("湖南省",299),("台湾省",399),("广东省",499)]
map.add("测试地图",data,"china")
#设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True,
    is_piecewise=True,
    pieces=[
        {"min" :1,"max":9,"label":"1-9","color":"#CCFFFF"},
        {"min" :10,"max":99,"label":"10-99","color":"#FF6666"},
        {"min" :100,"max":500,"label":"100-500","color":"#990033"}
    ]
                            )
)
map.render()


#基础柱状图
from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
bar1 = Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))      #确定y轴数据，并把数字标签移到右边
bar1.reversal_axis()    #反转x,y轴

bar2 = Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,40,30],label_opts=LabelOpts(position="right"))      #确定y轴数据，并把数字标签移到右边
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[60,50,50],label_opts=LabelOpts(position="right"))      #确定y轴数据，并把数字标签移到右边
bar3.reversal_axis()
#设置时间线
timeline = Timeline({"theme":ThemeType.LIGHT})
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")
#自动播放设置
timeline.add_schema(
    play_interval = 1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play = True
)

timeline.render("基础时间线柱状图.html")

