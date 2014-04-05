from rest_framework import serializers
from voting.models import (SongPoll, Song)

class SongPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongPoll

class SongSerializer(serializers.ModelSerialzier):
    class Meta:
        model = Song
