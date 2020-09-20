from importlib import reload

from zoo import animals
from zoo.delivery import deliver


def main():
    while True:
        print(f'available animals: {", ".join(animals.ANIMALS.keys())}')

        action = input().strip().lower()

        if action == 'exit':
            raise KeyboardInterrupt()

        if action in animals.ANIMALS:
            animals.ANIMALS[action].speak()
            print('============')
            print()
            continue

        print(f'{action} is not available. Wait a second...')
        deliver(action)
        reload(animals)
        print('============')
        print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Bye-bye!')
        exit()
