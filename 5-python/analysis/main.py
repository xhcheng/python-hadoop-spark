"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用自雷实现具体功能
3.读取文件，生产数据对象
4.进行数据需求的逻辑计算（计算每一天的销售额）
5.通过PyEcharts进行图形绘制
"""

from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取文件，生产数据对象
text_file_reader = TextFileReader('1.txt')
json_file_reader = JsonFileReader('2.txt')

jan_data: list = text_file_reader.read_data()
# feb_data: list = json_file_reader.read_data()
# # 将2个月份的数据合并为1个list来存储
# all_data: list = jan_data + feb_data
all_data = jan_data

# 开始数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日记已经有记录了，所以和老记录累加即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 通过PyEcharts进行图形绘制
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')

)

bar.render("每日销售额柱状图.html")

