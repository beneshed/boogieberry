from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import (ListView, DetailView)

from rest_framework import viewsets

from voting.serializers import (SongPollSerializer, SongSerializer, Vote)
from voting.models import (SongPoll, Song, Vote)
# Create your views here.

class SongPollViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SongPoll.objects.all()
    serializer_class = SongPollSerializer

class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = Song

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = Vote

