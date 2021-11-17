from googletrans import Translator
translator = Translator()

try:
    with open(r'.\IO\translator\text.txt', mode='r') as my_file:
        text1 = my_file.read()
except FileNotFoundError as err:
    print(err)
else:
    translation = translator.translate(text1)
    with open(r".\IO\translator\result.txt", mode='w') as my_file2:
        my_file2.write(translation.text)
