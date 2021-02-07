from abc import ABCMeta


class Zoo:

    def __init__(self, name) -> None:
        self.name = name
        self.zoo = set()

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError(f'expected an Animal instance')
        self.zoo.add(animal)

    def remove_animal(self, animal):
        if animal not in self.zoo:
            raise AttributeError(f'no attribute {animal}')
        self.zoo.remove(animal)

    def __repr__(self) -> str:
        return f'Zoo({self.name!r})'

    def __contains__(self, animal):
        return animal in self.zoo

    @property
    def size(self):
        return len(self.zoo)

    def __getattr__(self, item):
        try:
            count = sum(isinstance(i, eval(item)) for i in self.zoo)
            if count:
                self.__dict__[item] = count
        except NameError as e:
            print(e)


class Animal(metaclass=ABCMeta):
    def __init__(self, variety, figure, character):
        self.variety = 'other'
        self.figure = 0
        self.character = 'other'

    @property
    def is_beast(self):
        if self.variety == 'eat_meat' and self.figure >= 1 and self.character == 'savage':
            return True
        else:
            return False


class Cat(Animal):
    sound = 'miao'

    def __init__(self, name, variety, figure, character):
        super().__init__(variety, figure, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_beast:
            return False
        else:
            return True

    @classmethod
    def get_sound_(cls):
        return cls.sound


class Dog(Animal):
    sound = 'wang'

    def __init__(self, name, variety, figure, character):
        super().__init__(variety, figure, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_beast:
            return False
        else:
            return True


if __name__ == "__main__":
    z = Zoo('时间动物园')

    cat1 = Cat('大花猫1', '食肉', '小', '温顺')

    z.add_animal(cat1)

    have_cat = hasattr(z, 'Cat')
