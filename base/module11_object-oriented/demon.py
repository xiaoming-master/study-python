"""
@author:ming
@file:demon.py
@time:2021/10/19
"""
"""
 类属性：它被所有类对象的实例对象(实例方法)所共有，在内存中只存在一个副本，和C++中类的静态成员变量有点类似，不能通过实列修改类属性
 实列属性：
    如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性，
    并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。
"""


class Biology:
    type = '生物'

    def __init__(self, name):
        self.name = name


# b1 = Biology("动物")
# b2 = Biology("植物")
# print(b1.name) 生物
# b1.name = "hhh"
# print(b1.name) hhh
# print(b2.name) 生物

class Human(Biology):
    type = "人类"

    def __init__(self, name):
        super().__init__(name)

    def eat(self, biology):
        pass


class Animal(Biology):
    type = "动物"

    def __init__(self, name):
        super().__init__(name)

    def eat(self, biology):
        pass


class Plant(Biology):
    type = "植物"

    def __init__(self, name):
        super().__init__(name)

    def photosynthesis(self):
        print(self.name + "光合作用")
        return


class Student(Human):
    def __init__(self, name, age, sex, stu_id):
        super().__init__(name)
        self.age = age
        self.sex = sex
        self.stu_id = stu_id

    # 多态
    def study(self, biology):
        print("这是" + biology.name)
        return


class Teacher(Human):
    def __init__(self, name, age, sex, teaching_age):
        super().__init__(name)
        self.age = age
        self.sex = sex
        self.teaching_age = teaching_age


class Horse(Animal):
    type = "马"

    def __init__(self, name):
        super().__init__(name)

    def eat(self, plant):
        print(self.name + "吃" + plant.name)

    def __str__(self):
        return "我是" + self.name


class Grass(Plant):
    type = "草"

    def __init__(self, name):
        super().__init__(name)

    # 重写str方法，在print()函数中自动调用
    def __str__(self):
        return "我是" + self.name


horse = Horse("汗血宝马")
grass = Grass("香草")
stu = Student("小明", 22, 1, 1001)
stu.study(horse)  # 这是汗血宝马

print(horse)  # 我是汗血宝马
print(grass)  # 我是香草

grass.photosynthesis()
horse.eat(grass)

# 动态绑定属性
grass.color = 'green'


def get_color():
    print("我是绿色的草")
    return


# 动态绑定方法
grass.get_color = get_color
print(grass.color)
grass.get_color()
