class Animal:
    def eat(self):
        print(f'{self.__class__.__name__} say ololo...')


class Cat(Animal):
    def meow(self):
        print(f'{self.__class__.__name__} say meow...')

    def eat(self):
        print(f'{self.__class__.__name__} eats fish...')


class Dog(Animal):
    def bark(self):
        print(f'{self.__class__.__name__} say grrrrr...')

    def eat(self):
        print(f'{self.__class__.__name__} eats meat...')


class CatDog(Dog, Cat):
    def eat(self):
        print(f'{self.__class__.__name__} eats meat and fish...')


catdog = CatDog()

#: TODO: super(Cat, catdog).eat() -- WTF?
#: TODO: super(Dog, catdog).eat() -- WTF?
