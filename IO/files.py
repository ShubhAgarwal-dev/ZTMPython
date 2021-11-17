# How to Open File in proper way so not required to close it
#    # Default mode of open is 'r'
#    # To write mode = 'w'
#    # To read and write , mode = 'r+'
#    # Append mode, mode = 'a'

with open(r'.\IO\text.txt', mode='r+') as my_file:
    # print(my_file.read())
    text = my_file.write("**")

with open(r'.\IO\text2.txt', mode='a') as my_file2:
    text2 = my_file2.write(":)")

with open(r".\IO\text3.txt", mode='w') as my_file3:
    text3 = my_file3.write("Hello, I am Shubh Agarwal\nYES")

print(text)
print(text2)
print(text3)

'''
When we write to a file the cursor resets and we overwrite everything written before it.
# info:
# -> Mode:'r+' Read plus overwrite the content coming in the way but does not not make a new file if not present before
# -> Mode:'w' Write overwrite everythong written before and write new after that, and even make a new file is not present before
# -> Mode;'a' Append writes at last of file and also make a new file of not present before
# NO: Do not use absolute file path
'''
