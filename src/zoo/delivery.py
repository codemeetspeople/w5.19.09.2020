from string import ascii_lowercase
from random import choice

from zoo.settings import ANIMALS_PATH


CLASS_TEMPLATE = (
    '\n@animal_in_zoo\n'
    'class {class_name}(Animal):\n'
    '    @classmethod\n'
    '    def speak(cls):\n'
    '        print(f\'{{cls.get_title()}} say {sound}-{sound}\')\n\n'
)


def deliver(animal):
    sound = ''.join([choice(ascii_lowercase) for _ in range(4)])
    class_name = animal.capitalize()
    class_source = CLASS_TEMPLATE.format(class_name=class_name, sound=sound)

    with open(ANIMALS_PATH, 'r') as source:
        source_code = source.read()

    with open(ANIMALS_PATH, 'w') as destination:
        destination.write(f'{source_code}{class_source}')
