from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.dates import DayArchiveView, DateDetailView, ArchiveIndexView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import Show, Song, Venue
# Create your views here.


class ShowListView(ArchiveIndexView):
    model = Show
    date_field = "date"

    def get_queryset(self):
        queryset = super(ShowListView, self).get_queryset()
        #
        # q = self.request.GET.get("q")
        #
        # if q:
        #     return queryset.filter(slug=q)
        return queryset


class ShowDayView(DayArchiveView):
    model = Show
    date_field = 'date'
    year_format = '%Y'
    month_format = '%m'
    day_format = '%d'



class ShowDetailView(DateDetailView):
    model = Show
    date_field = 'date'
    year_format = '%Y'
    month_format = '%m'
    day_format = '%d'
    template_name = 'setlists/show_detail.html'

class SongListView(ListView):
    model = Song

    def get_queryset(self):
        queryset = super(SongListView, self).get_queryset()
        #
        # q = self.request.GET.get("q")
        #
        # if q:
        #     return queryset.filter(slug=q)
        return queryset


class SongDetailView(DetailView):
    model = Song
    slug_field = 'slug'


class VenueListView(ListView):
    model = Venue

    def get_queryset(self):
        queryset = super(VenueListView, self).get_queryset()
        #
        # q = self.request.GET.get("q")
        #
        # if q:
        #     return queryset.filter(slug=q)
        return queryset


class VenueDetailView(DetailView):
    model = Venue
    slug_field = 'slug'
