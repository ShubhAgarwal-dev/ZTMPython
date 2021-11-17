from re import search, compile

pattern = compile('this')
pattern2 = compile('please!')
string = 'Search this inside of this text please!'

a = pattern.search(string)
print(a.group())
print(a.span())
print(a.end())
print()

b = pattern.findall(string)
print(b)

print(pattern2.fullmatch(string))

print(pattern2.match(string))

'''
we could have also used print('thin' in string)
but re is much more powerful

.group() returns all subgroup of match
re.compile returns regular expression object and be used to search futher
search return Match Object or None
findall finds all instances of match and return list of pattern 
fullmatch go for full match and return match object
match only want starting to be same rest could be anything and return match object 
'''
