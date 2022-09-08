# import json
#
# data = [{"name":"张大三","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]
# json_str = json.dumps(data,ensure_ascii=False)
# print(type(json_str))
# print(json_str)
#
# d = {"name":"周杰伦","addr":"台北"}
# json_str = json.dumps(d)
# print(type(json_str))
# print(json_str)
#
#
# s = '[{"name":"张大三","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]'
# l = json.loads(s)
# print(type(l))
# print(l)
#
# s = '{"name":"周杰伦","addr":"台北"}'
# l = json.loads(s)
# print(type(l))
# print(l)


# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,TooltipOpts
#
# line = Line()
# line.add_xaxis(["中国","美国","日本"])
# line.add_yaxis("GDP",[30,20,10])
#
# line.set_global_opts(
#     title_opts=TitleOpts("GDP展示",pos_left="center",pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True),
#     tooltip_opts=TooltipOpts(is_show=True)
#
# )
#
# line.render()


import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,TooltipOpts

f_us = open("美国.txt",'r',encoding='UTF-8')
us_data = f_us.read()

f_jp = open("日本.txt",'r',encoding='UTF-8')
jp_data = f_jp.read()

f_in = open("印度.txt",'r',encoding='UTF-8')
in_data = f_in.read()

us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
in_data = in_data.replace("jsonp_1629350745930_63180(","")

us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

us_dict = json.loads(us_data)
us_trend = us_dict['data'][0]['trend']
us_x_data = us_trend['updateDate'][:314]
us_y_data = us_trend['list'][0]['data'][:314]
# print(us_y_data)

jp_dict = json.loads(jp_data)
jp_trend = jp_dict['data'][0]['trend']
jp_x_data = jp_trend['updateDate'][:314]
jp_y_data = jp_trend['list'][0]['data'][:314]
# print(us_y_data)

in_dict = json.loads(in_data)
in_trend = in_dict['data'][0]['trend']
in_x_data = in_trend['updateDate'][:314]
in_y_data = in_trend['list'][0]['data'][:314]
# print(us_y_data)

line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数",us_y_data)
line.add_yaxis("日本确诊人数",jp_y_data)
line.add_yaxis("印度确诊人数",in_y_data)

line.render()

f_us.close()
f_jp.close()
f_in.close()



































