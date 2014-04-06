import django_filters
from rest_framework import serializers
from voting.models import (Song, Vote)

class VoteSerializer(serializers.ModelSerializer):
    song_id = serializers.RelatedField(many=False)
    class Meta:
        model = Vote

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song


