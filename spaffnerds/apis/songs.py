# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from sqlalchemy.sql import func

from spaffnerds.extensions import api
# from spaffnerds.music.forms import LoginForm
# from spaffnerds.user.forms import RegisterForm
# from spaffnerds.user.models import User
from spaffnerds.utils import flash_errors
from spaffnerds.music.models import Song

blueprint = api.create_api_blueprint(
    'songs',
    Song,
    methods=['GET', 'POST', 'DELETE']
    )
