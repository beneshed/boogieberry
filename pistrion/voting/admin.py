from django.contrib import admin
from voting.models import Vote, Song

# Register your models here.
class VoteAdmin(admin.ModelAdmin):
    pass
class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vote, VoteAdmin)
admin.site.register(Song, SongAdmin)
