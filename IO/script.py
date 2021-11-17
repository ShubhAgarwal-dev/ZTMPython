my_file = open(r'IO/text.txt')

print(my_file.read())  # cursor is not at end line

print(my_file.read())  # it would not read it more than once as it read as cursor

my_file.seek(0)  # Index of where to put cursor
print(my_file.read())

my_file.seek(5)
print(my_file.read())

my_file.seek(0)
print(my_file.readlines())  # convert full text to list

my_file.close()  # to close the file
