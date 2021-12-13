import smtplib
from email.message import EmailMessage
from password import eid, eid_password

email = EmailMessage()
email['from'] = 'Radium Kircket'
email['to'] = 'shubhagarwa8888@gmail.com'
email['subject'] = 'Hello, you are selected to do automation'

email.set_content(
    'I am very happy that I, Shubh Agarwal could be doing automation now.')

'''
# to send the email content from html:

from string import Template
from pathlin import path

html = Template(Path('index.html).read_text())
# you can have variables in the HTML file like($name, $a and many more) 
    # any you can substitute them here.
# Suppose the html had variable $name in the <body>...$name, $age </body>



and replace email.set_content with
email.set_content(html.substitute({'name': 'Shubh', 'age': '18'}), 'html')
'''

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user=eid, password=eid_password)
    smtp.send_message(email)
    print('done')
