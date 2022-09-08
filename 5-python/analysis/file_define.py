"""
和文件相关的类定义
"""
import json
from data_define import Record

#先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:

    def read_data(self) -> list:
        """读取文件的数据，读取的每一条数据都转换为Record对象，将他们都封装到list内返回即可"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list:
        f = open(self.path, 'r', encoding='UTF-8')

        record_list: list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(float(data_list[2])), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list:
        f = open(self.path, 'r', encoding='UTF-8')

        record_list: list = []
        for line in f.readlines():
            data_dict = json.load(line)
            record = Record(data_dict['date'], data_dict['order_id'], int(float(data_dict['money'])), data_dict['province'])
            record_list.append(record)

        f.close()
        return record_list




if __name__=='__main__':
    text_file_reader = TextFileReader('1.txt')
    json_file_reader = JsonFileReader('2.txt')


    list1= text_file_reader.read_data()
    list2 = json_file_reader.read_data()
