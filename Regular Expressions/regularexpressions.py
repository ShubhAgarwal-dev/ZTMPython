from re import search, compile

pattern = compile('this')
string = 'Search this inside of text please!'

a = search(pattern, string)
print(a.group())
