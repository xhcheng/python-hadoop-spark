"""
文件处理相关工具
"""
def print_file_info(file_name):
    """
    文件读取并打印
    :param file_name: 即将被读取的文件路径
    :return:None
    """
    f = None
    try:
        f = open(file_name,'r',encoding='UTF-8')
        content = f.read()
        print(content)
    except Exception as e:
        print(f"程序出现异常，原因是：{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    """
    文件追加
    :param file_name: 需要被追加内容的文件路径
    :param data: 需要被追加的内容
    :return: None
    """
    f = open(file_name,'a',encoding='UTF-8')
    f.write(data)
    f.close()

if __name__=='__main__':
    print_file_info("../5-python/1.txt")
    append_to_file("../5-python/test_append.txt","1111111111111111")