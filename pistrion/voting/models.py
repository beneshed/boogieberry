from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from localflavor.us.models import PhoneNumberField

# Create your models here.
class Vote(TimeStampedModel):
    number = PhoneNumberField()
    song_id = models.ForeignKey('Song')

    def __unicode__(self):
        return u'%s' % str(self.number)


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
    duration = models.IntegerField(default=0)
    shortUrl = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.name
