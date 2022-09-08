"""
本代码演示了：
-注释
-变量
"""

# 这是一个注释

# money =50
# print("钱包还有：",money)
# money=money-10
# print("买了10元冰淇淋，钱包还有：",money)
#
# name = "黑马程序员"
# message = "学IT就来%s" % name
# print(message)
#
# class_num = 57
# avg_salary = 16781
# message = "Python大数据学科，北京%s期，毕业平均工资：%d" % (class_num,avg_salary)
# print(message)
#
# name = "传智播客"
# setup_year = 2006
# stock_price = 19.99
# message = "%s,成立于：%d，今天的股价是：%f" % (name,setup_year,stock_price)
# print(message)

# num1 = 11
# num2 = 11.345
# print("数字11宽度限制5，结果是：%5d" % num1)
# print("数字11宽度限制1，结果是：%1d" % num1)
# print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
# print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2)

# name = "传智播客"
# set_up_year = 2006
# stock_price = 19.99
# print(f"我是{name},我成立于：{set_up_year}年，我今天的股价是：{stock_price}")

# print("1*1的结果是：%d" % (1*1))
# print(f"1*2的结果是：{1*2}")
# print("字符串在Python中的类型名称是：%s" % type("字符串"))

# name = "传智播客"
# stock_price = 19.99
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days =7
#
# finally_stock_price = stock_price*stock_price_daily_growth_factor**growth_days
#
# print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
# print("每日增长系数是：%.1f,经过%d天后的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,finally_stock_price))


# name = input("请告诉我你是谁？")
# print("我知道了，你是%s" % name)

# import random
#
# num = random.randint(1,10)
# n = int(input("请输入你的猜测:"))
#
#
# def test(n,num):
#     if n > num:
#         n = int(input("你的猜测过大，请再次猜测："))
#         test(n,num)
#     elif n < num:
#         n = int(input("你的猜测过小，请再次猜测："))
#         test(n,num)
#     else:
#         print("猜测正确！%d" % num)
#
# test(n,num)

# i = 1
# n = 0
#
# while i<=100:
#     n+=i
#     i+=1
#
# print(n)


# n=1
#
# while n<=9:
#     i = 1
#     while i<=n:
#         print(f"{i}*{n}={i * n}\t", end='')
#         i+=1
#     print()
#     n+=1


# name = "hello world"
#
# for i in name:
#     print(i)

# for x in range(5):
#     print(x)
#
# for x in range(1,10):
#     print(x)
#
# for x in range(1,10,2):
#     print(x)


# i=0
# for x in range(100):
#     if x%2==0:
#         i+=1
# print(i)

# for i in range(5):
#     print('a')
#
# print(i)



# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}\t",end='')
#     print()


# def my_len(data):
#     count = 0
#     for i in data:
#         count+=1
#     print(f"字符串{data}的长度是{count}")
#
# my_len("hello")

# def add(x,y):
#     """
#     :param x:
#     :param y:
#     :return:
#     """
#     result = x + y
#     print(f"{x}+{y}的计算结果是：{result}")
#     return result
#
#
# add(5,6)

# name = None
# name = "aaa"
# name = 123
# name = 1.2345
# print(type(name))

# my_list = [1,2,3]
# my_list.insert(0,"itheima")
# print(my_list)

# my_list = ["itheima","itcast","python"]
# print(my_list.index("itcast"))

# my_list = [1,2,3]
# my_list.append(4)
# print(my_list)
#
# my_list = [1,2,3]
# my_list.append([4,5,6])
# print(my_list)

# my_list = [1,2,3]
# my_list.extend([4,5,6])
# print(my_list)
#
# del my_list[0]
# print(my_list)
#
# my_list.pop(1)
# print(my_list)


# my_list = [1,2,3,4,5,6,6]
# my_list.remove(5)
# print(my_list)
#
# print(my_list.count(6))
#
# my_list.clear()
# print(my_list)

# my_list = [0,1,2,3,4,5]
# print(len(my_list))


# my_list = [1,2,3,4,5]
#
# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index+=1
#
# for i in my_list:
#     print(i)

# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# n_list = []
# for i in my_list:
#     if i%2==0:
#         n_list.append(i)
#
# print(n_list)

# str = "itheima itcast boxuegu"
# print(str)
# str1 = str.replace(" ","|")
# print(str1)
# str2 = str1.split("|")
# print(str2)

# str = "万过薪月，员序程马黑来，nohtyP学"
# str1 = str[9:4:-1]
# print(str1)

# set = {'hello','world','!','hello'}
# print(set)

# my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
# em_set = set()
#
# for i in my_list:
#     em_set.add(i)
#
# print(em_set)


# em_dict = {
#     "王力宏":{"部门":"科技部","工资":3000,"级别":1},
#     "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
#     "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
#     "张学友":{"部门":"科技部","工资":4000,"级别":1},
#     "刘德华":{"部门":"市场部","工资":6000,"级别":2},
# }
#
# for item in em_dict:
#     if em_dict[item]["级别"] ==1:
#         em_dict[item]["工资"] +=1000
#         em_dict[item]["级别"] = 2
#
# print(em_dict)





# lucky = []
#
# def luckys():
#     global lucky
#     num = int(input("请输入数字："))
#     nums = range(1,num+1)
#     i = set(nums).pop()
#     if i%6 == 0:
#         lucky.append(i)
#     print(nums)
#     print(lucky)
#
# while True:
#     luckys()


# import random
#
# class_rom = [[],[],[]]
# teachers = ['A','B','C','D','E','F','G','H']
#
# for i in teachers:
#     n = random.randint(0,2)
#     class_rom[n].append(i)
#
# print(class_rom)


# def test_func(compute):
#     result = compute(1,2)
#     print(result)
#
# def compute(x,y):
#     return x+y
#
# test_func(compute)
#
# test_func(lambda x,y:x-y)


# f = open("1.txt","r",encoding="UTF-8")
# for line in f:
#     print(line)
#
# f.close()
#
# with open("1.txt","r",encoding="UTF-8") as f:
#     line = f.readlines()
#
# print(line)

# f = open("1.txt","r",encoding="UTF-8")
#
# print(f.read(10))
# print(f.read())
#
# f.close()


# n = 0
# f = open("1.txt","r",encoding="UTF-8")
# for line in f:
#     list = line.split()
#     for i in list:
#         if i == "itheima":
#             n += 1
#
# print(n)
#
# f.close()

# f = open("test.txt","w",encoding="UTF-8")
# f.write("hello world!")
#
# #f.flush()
# f.close()

# fr = open("2.txt","r",encoding="UTF-8")
# fw = open("2.bak.txt","w",encoding="UTF-8")
# for line in fr:
#     line = line.strip()
#     if line.split(",")[4] == "正式":
#         fw.write(line)
#         fw.write("\n")
#
# fr.close()
# fw.close()

# f = open("3.txt","a",encoding="UTF-8")
# f.write(a)
# f.close()


# try:
#     open("linux.txt","r")
# except:
#     open("linux.txt","w")

# try:
#     print(name)
# except NameError as e:
#     print(e)

# try:
#     print(1/0)
# except (NameError, ZeroDivisionError) as e:
#     print(e)


# try:
#     print(name)
# except Exception as e:
#     print(e)


# try:
#     f = open('test.txt', 'r')
# except Exception as e:
#     f = open('test.txt', 'w')
# else:
#     print('没有异常，真开心')
# finally:
#     f.close()


# import time
#
# print("开始")
# time.sleep(1)
# print("结束")

# from time import *
#
# sleep(5)
# print("hello")


# import my_module1
#
# my_module1.test(1,2)

# from my_module1 import test
#
# test(1,2)

# from my_module1 import test
# from my_module2 import test
#
# test(1,2)

# from my_module1 import *
#
# test(1,2)

# import my_package.my_module1
# import my_package.my_module2


# import my_utils.str_util
# from my_utils import file_util
#
# print(my_utils.str_util.str_reverse("黑马程序员"))
# print(my_utils.str_util.substr("黑马程序员",1,3))
#
# file_util.print_file_info("1.txt")
# file_util.append_to_file("test_append.txt","1111111111111111")








