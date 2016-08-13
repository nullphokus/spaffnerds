# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from sqlalchemy.sql import func

from spaffnerds.extensions import login_manager
# from spaffnerds.music.forms import LoginForm
# from spaffnerds.user.forms import RegisterForm
# from spaffnerds.user.models import User
from spaffnerds.utils import flash_errors

from spaffnerds.music.models import Song
from spaffnerds.music.models import Venue
from spaffnerds.music.models import Show

import datetime

blueprint = Blueprint('music', __name__, static_folder='../static')


@blueprint.route('/')
def home():
    """ 
        Home page
    """

    ## upcoming shows
    current_time = datetime.datetime.utcnow()
    upcoming_shows = Show.query.filter_by(Show.date >= current_time).order_by()
    return render_template('music/home.html')

@blueprint.route('/songs/')
def songs():
    """Register new user."""
    songs = Song.query.all()
    return render_template('music/songs.html', data=songs)

@blueprint.route('/songs/<name>')
def song(name):
    """Register new user."""
    name = name.lower().replace(' ', '-')
    song = Song.query.filter_by(system_name=name).first_or_404()
    # venues = song.venues

    # get date last played

    return render_template('music/song.html', data=song)

@blueprint.route('/venues/')
def venues():

    venues = Venue.query.order_by(Venue.name).all()

    # date first played
    # date last played
    # times played
    # stats = Venue.query(func.min(date))
    return render_template('music/venues.html', data=venues)

@blueprint.route('/venues/<name>')
def venue(name):
    """Register new user."""
    venue = Venue.query.filter_by(name=name).first_or_404()
    return render_template('music/venue.html', data=venue)

@blueprint.route('/shows/')
def shows():
    """Register new user."""
    shows = Show.query.order_by(Show.date.desc()).all()
    return render_template('music/shows.html', data=shows)

@blueprint.route('/shows/<date>', methods=['GET', 'POST'])
def show(date):
    """Register new user."""
    show = Show.query.filter_by(date=date).first_or_404()

    songs = {}
    notes = []
    for song in show.song_assoc:
        song_ = (song.track_order, song.song_name, song.song_sys_name, song.segued, bool(song.song_notes))
        if song.song_notes:
            notes.append(song.song_notes)
        sset = song.show_set.replace('E1', 'Encore')

        songs.setdefault(sset, []).append(song_)

    print songs
    return render_template('music/show.html', data=show, songs_data=songs,notes=notes)
