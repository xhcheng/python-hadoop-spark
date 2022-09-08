class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def __str__(self):
        return f"名字：{self.name}年龄：{self.__age}"

    def __brain(self):
        print("大脑")

xm = Person("小明",18)
print(xm)
# print(xm.__age)
# print(xm._Person__age)
# print(xm.__dict__)

# xm.__age = 20
# print(xm)
# print(xm.__age)

