import os
from sys import argv
from PIL import Image
from pathlib import Path

source_folder = Path(argv[1])
destination_folder = Path(argv[2])

if not os.path.exists(source_folder):
    print(f'{source_folder} does not exists.')
    source_folder = Path(input("Source folder:"))

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

current_path = os.getcwd()

os.chdir(source_folder)
for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg'):
        os.chdir(current_path)
        os.chdir(source_folder)
        clean_name = os.path.splitext(file)[0]
        img = Image.open(f'{file}')
        os.chdir(current_path)
        os.chdir(destination_folder)
        img.save(f'{clean_name}.png', 'png')
        print(f"{file} converted")
