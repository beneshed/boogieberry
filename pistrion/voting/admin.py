from django.contrib import admin
from voting.models import SongPoll, Vote, Song

# Register your models here.
class SongPollAdmin(admin.ModelAdmin):
    pass
class VoteAdmin(admin.ModelAdmin):
    pass
class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(SongPoll, SongPollAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Song, SongAdmin)
