# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'shows/$',
        view=views.ShowListView.as_view(),
        name='show-list'
    ),
    url(
        regex=r'shows/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$',
        view=views.ShowDayView.as_view(),
        name='show-day'
    ),
    url(
        regex=r'shows/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$',
        view=views.ShowDetailView.as_view(),
        name='show-detail'
    ),

    url(
        regex=r'songs/$',
        view=views.SongListView.as_view(),
        name='song-list'
    ),
    url(
        regex=r'songs/(?P<slug>[\w-]+)$',
        view=views.SongDetailView.as_view(),
        name='song-detail'
    ),

    url(
        regex=r'venues/$',
        view=views.VenueListView.as_view(),
        name='venue-list'
    ),
    url(
        regex=r'venues/(?P<slug>[\w-]+)$',
        view=views.VenueDetailView.as_view(),
        name='venue-detail'
    ),
]
