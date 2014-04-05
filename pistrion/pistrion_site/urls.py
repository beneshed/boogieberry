from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from voting.views import SongPollViewSet, SongViewSet, VoteViewSet 
from voting.models import SongPoll, Song, Vote

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'songpolls', SongPollViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'songs', SongViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pistrion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include(router.urls)),
)
