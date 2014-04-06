from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACec0c7c5211527b56dedd223ea469e3bc"
auth_token  = "a79b8b5c99c2cf699782fe2026cf1036"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(body="This is a message from yourself.",
    to="+18049127024",    # Replace with your phone number
    from_="+17039978436") # Replace with your Twilio number
print message.sid