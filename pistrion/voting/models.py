from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

# Create your models here.
class SongPoll(TimeStampedModel):
    creator = models.ForeignKey(User)
    votes = models.ManyToManyField('Song')

    def __unicode__(self):
        return '%s' % self.id

class Song(TimeStampedModel):
    song_id = models.IntegerField()
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    artistKey = models.CharField(max_length=100)
    embedUrl = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.title
