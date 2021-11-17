from re import search, compile

pattern = compile('this')
string = 'Search this inside of text please!'

a = pattern.search(string)
print(a.group())
