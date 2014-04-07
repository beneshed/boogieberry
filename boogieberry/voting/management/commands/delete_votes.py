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
        Vote.objects.all().delete()
