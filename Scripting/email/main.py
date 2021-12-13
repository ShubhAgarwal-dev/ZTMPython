import smtplib
from email.message import EmailMessage
from password import eid, eid_password

email = EmailMessage()
email['from'] = 'Radium Kircket'
email['to'] = 'shubhagarwa8888@gmail.com'
email['subject'] = 'Hello, you are selected to do automation'

email.set_content(
    'I am very happy that I, Shubh Agarwal could be doing automation now.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user=eid, password=eid_password)
    smtp.send_message(email)
    print('done')
