class Animal:
    def eat(self):
        pass
    def drink(self):
        pass
    def run(self):
        pass
    def sleep(self):
        pass

    # 类方法：前提：方法中不需要实例属性，用到了类属性，可以将这个方法定义为类方法
    @classmethod
    def func(cls):# cls表示的类对象
        pass
    # 静态方法：前提：方法中不需要实例属性，也不使用类属性，可以将这个方法定义为静态方法
    @staticmethod
    def func1():
        pass

class Dog(Animal):
    def bark(self):
        pass

class XiaoTianQuan(Dog):
    def fly(self):
        pass
    def bark(self):
        print("houhou")

