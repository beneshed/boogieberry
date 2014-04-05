from rest_framework import serializers
from voting.models import (SongPoll, Song, Vote)

class SongPollSerializer(serializers.ModelSerializer):
    choices = serializers.RelatedField(many=True)
    class Meta:
        model = SongPoll

class VoteSerializer(serializers.ModelSerializer):
    vote_id = serializers.RelatedField(many=False)
    poll_id = serializers.RelatedField(many=False)
    class Meta:
        model = Vote

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
