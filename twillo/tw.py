from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC12446ff63d16f5749cf9d3d59c0465dc'
auth_token = '77672a18715f646025afea018ef1094d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Jonathan, Male champaign found.",
                     from_='+1(312) 471-0558',
                     to='+13123588613'
                 )

print(message.sid)


