from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = [
    ("北京市",99),
    ("上海市",199),
    ("湖南省",299),
    ("台湾省",399),
    ("广东省",399)
]
map.add("测试地图",data,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_piecewise=True,
        is_show=True
    )
)
map.render()

from pyecharts import options as opts
f = open()
data_lines = f.readlines()
f.close()
data_lines.pop(0)
data_dict = {}
for line in data_lines:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    gdp = float(line.split(',')[2])
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append([country,gdp])
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year]=sorted(key=lambda element:element[1],reverse=True)
    year_data=data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1])
    bar = Bar()


