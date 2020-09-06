# -*- coding:utf-8 -*-
"""
具体要求：

定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
"""
from abc import ABCMeta, ABC
from abc import abstractmethod

# shout

vorous_map = {
    "食肉": 30,
    "杂食": 20,
    "graminivorous": 10,
}

somatotype_map = {
    "大": 30,
    "中等": 20,
    "小": 10,
}

characteristic_map = {
    "凶猛": 200,
    "温顺": 100
}


class Animal(ABC):
    '''
    def __new__(cls, *args, **kwargs):
        raise Exception("不允许实例化")
    '''

    def __init__(self, name, vorous, somatotype, characteristic):
        self.name = name
        self.vorous = vorous_map[vorous]
        self.somatotype = somatotype_map[somatotype]
        self.characteristic = characteristic_map[characteristic]

    @property
    def feral(self):
        if (self.somatotype >= 20 and self.characteristic >= 100 and self.vorous == 30):
            return True
        return False

    @abstractmethod
    def pet(self):
        pass


class Cat(Animal):
    bleat = None

    def __init__(self, name, vorous, somatotype, characteristic):
        self._is_pet = False
        return super().__init__(name, vorous, somatotype, characteristic)

    @property
    def pet(self):
        if(not self.feral):
            self._is_pet = True
            return True
        self._is_pet = False
        return False


class Dog(Animal):
    bleat = None

    def __init__(self, name, vorous, somatotype, characteristic):
        self._is_pet = False
        return super().__init__(name, vorous, somatotype, characteristic)

    @property
    def pet(self):
        if(not self.feral):
            self._is_pet = True
            return True
        self._is_pet = False
        return False


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animal_set = set()

    def add_animal(self, animal):
        if(not isinstance(animal, Animal)):
            print ("%s is not a Animal" % (animal))
            return

        if(id(animal) in self.animal_set):
            print(f"{animal.name} is already in the Zoo.")
            return

        setattr(self, animal.__class__.__name__, animal.__class__)
        self.animal_set.add(id(animal))


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('大花猫2', '食肉', '小', '温顺')
    print ("cat1 is a pet?",cat1.pet)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat2)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print (have_cat)
