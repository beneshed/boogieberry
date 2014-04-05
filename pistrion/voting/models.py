from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from localflavor.us.models import PhoneNumberField

# Create your models here.
class SongPoll(TimeStampedModel):
    creator = models.ForeignKey(User)
    choices = models.ManyToManyField('Song')

    def __unicode__(self):
        return '%s' % self.id


class Vote(TimeStampedModel):
    number = PhoneNumberField()
    vote_id = models.ForeignKey('Song')
    poll_id = models.ForeignKey('Vote')

    def __unicode__(self):
        return '%' % self.number


class Song(TimeStampedModel):
    songId = models.IntegerField()
    albumArtist = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=255, blank=True, null=True)
    albumKey = models.CharField(max_length=255)
    artistUrl = models.CharField(max_length=255)
    embedUrl = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    key = models.CharField(max_length=25)
    name = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.title
