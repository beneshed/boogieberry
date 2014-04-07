from django.http import HttpResponse
from collections import Counter
from twilio.rest import TwilioRestClient
from email.utils import parsedate_tz
from datetime import datetime
from time import time
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import (ListView, DetailView)

from rest_framework import viewsets
from rest_framework.decorators import api_view

from voting.serializers import (SongSerializer, VoteSerializer, ResultSerializer)
from voting.models import (Song, Vote, Result)
# Create your views here.

class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_fields = ('song_id__songId')

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

def trigger(request):
    account_sid = "ACb53930b6ce7c4b42f4a5c36d49a935b6"
    auth_token  = "06067fefdd853719c721ee6235b2215d"
    client = TwilioRestClient(account_sid, auth_token)

    resource_uri = "/2010-04-01/Accounts/ACb53930b6ce7c4b42f4a5c36d49a935b6/messages/"
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
            v = Vote(number=x.from_,song_id=s)
            v.save() 

    
    return HttpResponse(status=200)

def delete_votes(request):
    votes = Vote.objects.all().delete()
    return HttpResponse(status=200)
def retrieve(request):
    votes = Vote.objects.all()
    my_songids = []

    for vote in votes:
        my_songids.append( vote.__unicode__())

    print(my_songids)
    data = Counter( my_songids )
    print(data)
    
    (song_id, _) = data.most_common()[0]
    song_key = Song.objects.get( name=song_id ).key

    return HttpResponse(song_key)
