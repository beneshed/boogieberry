from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import (ListView, DetailView)

from rest_framework import viewsets
from rest_framework.decorators import api_view

from voting.serializers import (SongSerializer, VoteSerializer)
from voting.models import (Song, Vote)
# Create your views here.

class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_fields = ('song_id__songId')

'''
@api_view(['GET'])
def count_votes(request):
    votes = Vote.objects.all()
    votes = votes.query.group_by = ['song_id__songId')
    return votes
'''
