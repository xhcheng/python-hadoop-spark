# class Person:
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         return f"我是{self.name},我的体重{self.weight}"
#
#     def run(self):
#         self.weight -= 0.5
#
#     def eat(self):
#         self.weight +=1
#
#
# xiaoming = Person("小明",100)
# print(xiaoming)
# xiaoming.run()
# print(xiaoming.weight)
# xiaoming.eat()
# print(xiaoming.weight)

class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self) -> str:
        return f"家具：{self.name}，占地面积：{self.area}"

class House:
    def __init__(self,name,area):
        self.name = name #type: str
        self.area = area
        self.free = area
        self.items = []

    def __str__(self):
        return f"户型：{self.name}，面积：{self.area}，剩余面积：{self.free}，家具列表：{self.items}"

    def add_item(self,item: HouseItem):
        if self.free >= item.area:
            self.free -= item.area
            self.items.append(item.name)
        else:
            print("面积不够，无法放入")


house = House("A1",100)
print(house)

chair = HouseItem("椅子",1)
shafa = HouseItem("沙发",10)
print(chair)

house.add_item(chair)
print(house)
house.add_item(shafa)
print(house)






























