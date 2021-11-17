'''
regular expressions are a language init self
can study about it online but need not to memorize it
#-> Use regex101 to test and learn about all of it  and can go to regexone.com to learn about all of it
TODO : best way to search for regex is via google
    for eg.I went to search for regex for email addresses re on google and then i got emailregex.com
'''

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# it is used for re
email_address = 'shubhagarwa8888@gmail.com'
email_address2 = 'shubhagarwa8888gmail'

a = pattern.search(email_address)
b = pattern.search(email_address2)
print(a.group())
print(b)
