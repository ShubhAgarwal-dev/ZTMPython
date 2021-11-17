from io import UnsupportedOperation


try:
    with open(r'.\IO\sad.txt', mode='r') as file:
        file.read()
except FileNotFoundError as err:
    print(f"Requested file not found\n{err}")
except UnsupportedOperation as err:
    print(f'{err}')
