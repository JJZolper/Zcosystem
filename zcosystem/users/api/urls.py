from django.conf.urls import include, url

from views import *

from rest_framework import serializers

urlpatterns = [
    # Users API
    url(r'^users/$', UserProfileList.as_view(), name='user-profile-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserProfileRetrieveUpdateDestroy.as_view(), name='user-profile-retrieve-update-destroy'),
               
    # User Events API
    url(r'^users/events/$', UserEventList.as_view(), name='user-event-list'),
    url(r'^users/events/create/$', UserEventCreate.as_view(), name='user-event-create'),
    url(r'^users/events/(?P<pk>[0-9]+)/$', UserEventRetrieveUpdateDestroy.as_view(), name='user-event-retrieve-update-destroy'),
    url(r'^users/events/(?P<cityslug>[-a-zA-Z0-9_]+)/$', UserEventCityList.as_view(), name='user-event-city-list'),
]




