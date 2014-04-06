from twilio.rest import TwilioRestClient
from email.utils import parsedate_tz
from datetime    import datetime
from time        import time

# Your Account Sid and Auth Token from twilio.com/user/account
'''
for x in messages:
    x.date_created = datetime(*parsedate_tz(x.date_created)[:-3])

for x in messages:
    if "+17039978436" not in x.from_ and x.date_created > datetime(2014, 4, 5, 23, 0, 0, 0):
        print x.date_created
'''
def get_votes_after_date(timestamp, id1):
    account_sid = "ACec0c7c5211527b56dedd223ea469e3bc"
    auth_token  = "a79b8b5c99c2cf699782fe2026cf1036"
    client = TwilioRestClient(account_sid, auth_token)

    resource_uri = "/2010-04-01/Accounts/ACec0c7c5211527b56dedd223ea469e3bc/messages/"

    messages = client.messages.list()

    vote1 = 0
    vote2 = 0
    vote3 = 0
    vote4 = 0
    collectedMessages = ()

    # convert current dates to timestamps, college messages
    for x in messages: 
        x.date_created = x.date_created = datetime(*parsedate_tz(x.date_created)[:-3])
        if x.date_created > timestamp:
            if x.body == id1:
                vote1 += 1
            if x.body == (id1+1):
                vote2 += 1
            if x.body == (id1+2):
                vote3 += 1
            if x.body == (id1+3):
                vote4 += 1
    return [vote1, vote2, vote3, vote4]
