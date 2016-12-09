from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from braces.views import LoginRequiredMixin

from .models import Show, Song, Venue
# Create your views here.

class ShowListView(ListView):
    model = Show

    def get_queryset(self):
        queryset = super(ShowListView, self).get_queryset()
        #
        # q = self.request.GET.get("q")
        #
        # if q:
        #     return queryset.filter(slug=q)
        return queryset


class ShowDetailView(DetailView):
    model = Show


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
