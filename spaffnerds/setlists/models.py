from django.db import models
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    is_cover = models.BooleanField(default=0)
    lyrics = models.TextField(blank=True)
    # written_by = models.ForeignKey(Artist.name)

    def __str__(self):
        return self.title


class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
#     group = models.ForeignKey(Group.name)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Venue(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    loc_city = models.CharField(max_length=100, blank=True)
    loc_state = models.CharField(max_length=5, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    description = models.TextField(blank=True)
    is_closed = models.BooleanField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("venue-detail", kwargs={'slug': self.slug})


class Show(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    date_order = models.IntegerField(default=1)
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    songs = models.ManyToManyField(Song, through='ShowSongLink')

    def __str__(self):
        return str(self.date)


    def get_show_day(self):
        return reverse('setlists:show-day', kwargs = {
                        'year': self.date.strftime("%Y"),
                        'month': self.date.strftime("%m"),
                        'day': self.date.strftime("%d")})

    def get_absolute_show(self):
        return reverse('setlists:show-detail', kwargs = {
                        'year': self.date.strftime("%Y"),
                        'month': self.date.strftime("%m"),
                        'day': self.date.strftime("%d"),
                        'slug': self.date_order})


    class Meta:
        ordering = ('date', 'date_order')


class ShowSongLink(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    track_number = models.IntegerField()
    set = models.IntegerField(null=True, blank=True)  # (1,2,3,E1,E2)
    notes = models.TextField(blank=True)
    is_segued = models.BooleanField(default=0)
    # guest? link to artists

    def __str__(self):
        return "%s: %s - %s" % (self.show.date, self.track_number, self.song.title)

    class Meta:
        ordering = ('track_number',)


