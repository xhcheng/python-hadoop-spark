"""
字符串相关工具
"""
def str_reverse(s):
    """
    将字符串翻转
    :param s: 将被翻转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s, x, y):
    """
    按给定下标对字符串进行切片
    :param s: 即将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y:1]


if __name__=='__main__':
    print(str_reverse('黑马程序员'))
    print(substr('黑马程序员',1,3))
