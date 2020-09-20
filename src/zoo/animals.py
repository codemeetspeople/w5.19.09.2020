ANIMALS = {}


def animal_in_zoo(cls):
    if cls.get_title() not in ANIMALS:
        ANIMALS[cls.get_title()] = cls
    return cls


class Animal:
    @classmethod
    def get_title(cls):
        return cls.__name__.lower()

    @classmethod
    def speak(cls):
        raise NotImplementedError()


@animal_in_zoo
class Wolf(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_title()} say wooo-wooo')


@animal_in_zoo
class Horse(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_title()} say heee-haaa')


@animal_in_zoo
class Donkey(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_title()} say huuu-huuu')


@animal_in_zoo
class Tiger(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_title()} say oukt-oukt')


@animal_in_zoo
class Fox(Animal):
    @classmethod
    def speak(cls):
        print(f'{cls.get_title()} say dhej-dhej')
