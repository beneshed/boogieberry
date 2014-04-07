from django.contrib import admin
from voting.models import Vote, Song, Result

# Register your models here.
class VoteAdmin(admin.ModelAdmin):
    pass
class SongAdmin(admin.ModelAdmin):
    pass
class ResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vote, VoteAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Result,ResultAdmin)
