import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("黑马程序员",1,3))

file_util.append_to_file("D:/test.py","it")
file_util.print_file_info("D:/test.py")

import  json
data =[{"name":"李华","age":16},{"name":"张三","age":12},{"name":"小李","age":18}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts,VisualMapOpts

line = Line()
line.add_xaxis(["中国","英国","美国"])
line.add_yaxis("GDP",[30,20,10])
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()

