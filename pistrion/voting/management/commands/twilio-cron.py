from twilio.rest import TwilioRestClient
from email.utils import parsedate_tz
from datetime import datetime
from time import time
from django.core.management.base import BaseCommand, CommandError
from voting.models import Vote, Song

# Your Account Sid and Auth Token from twilio.com/user/account
class Command(BaseCommand):
    args = "FUCK THIS SHIT MAKE A NIGGA WANNA JUMP"
    help = "LET HIM GO"
    def handle(self, *args, **options):
        account_sid = "ACec0c7c5211527b56dedd223ea469e3bc"
        auth_token  = "a79b8b5c99c2cf699782fe2026cf1036"
        client = TwilioRestClient(account_sid, auth_token)

        resource_uri = "/2010-04-01/Accounts/ACec0c7c5211527b56dedd223ea469e3bc/messages/"

        messages = client.messages.list()

    # convert current dates to timestamps, college messages
        for x in messages: 
            x.date_created = x.date_created = datetime(*parsedate_tz(x.date_created)[:-3])
            try:
                int(x.body)
            except ValueError:
                continue 
            if(int(x.body) > 3000 or int(x.body)< 3101):
                try:
                    s = Song.objects.get(songId=x.body)
                except Song.DoesNotExist:
                    raise CommandError('Song "%s" does not exist' % poll_id)
                print("create")
                v = Vote(number=x.from_,song_id=s)
                v.save()
