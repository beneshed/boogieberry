from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from voting.views import SongViewSet, VoteViewSet, ResultViewSet, trigger, retrieve, delete_votes
from voting.models import Song, Vote

from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'votes', VoteViewSet)
router.register(r'songs', SongViewSet)
router.register(r'results', ResultViewSet)
#router2 = SimpleRouter()
#router2.register(r'result', count_votes)
#router.register(r'result', count_votes)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pistrion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^trigger/$', trigger),
    url(r'^retrieve/$', retrieve),
    url(r'^delete_votes/$', delete_votes),
    url(r'^api/', include(router.urls)),
)
