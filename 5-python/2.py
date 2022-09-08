
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"小猫的名字是{self.age}，年龄是：{self.age}")
    #打印对象时调用,未定义自动输出对象的引用地址
    def __str__(self):
        return f"小猫的名字是{self.age}，年龄是：{self.age}"
    def __del__(self):
        print(f"{self.name}对象被销毁")



blu_cat = Cat("蓝猫",2)
blu_cat.show_info()

black_cat = Cat("黑猫",3)
black_cat.show_info()
