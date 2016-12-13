from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.register_view, name='register'),

    url(r'^login/$', views.login_view, name='login'),

    # music/<some album id>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    #url(r'^album/add/$', views.CreateAlbum.as_view(), name='add-album'),

    url(r'^logout/$', logout, {'next_page': '/music/login/'}, name='logout')

    # music/<album id>/favorite/
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]