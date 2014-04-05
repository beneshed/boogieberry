from django.shortcuts import render, get_object_or_404, render_to_repsonse
from django.template import RequestContext
from django.views.generic import (ListView, DetailView)

from rest_framework import viewsets

from voting.serializers import (SongPollSerializer, SongSerializer)
from voting.models import (SongPoll, Song)
# Create your views here.

class SongPollViewset(viewsets.ReadOnlyModelViewSet):
    queryset = SongPoll.objects.all()
    serializer_class = SongPollSerializer

class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = Song


