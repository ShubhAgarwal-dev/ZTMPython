import apikey
# Can not share it because of secrecy of auth token
# import os
# Not required
from twilio.rest import Client, api


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ[apikey.account_id]
# auth_token = os.environ[apikey.auth_token]

account_sid = apikey.account_id
auth_token = apikey.auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hi there, I am using this automatic sms',
    from_=apikey.phone_number,
    to=apikey.my_phone_number
)

print(message.sid)
