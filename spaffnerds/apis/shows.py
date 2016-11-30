# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from sqlalchemy.sql import func

from spaffnerds.extensions import api
from spaffnerds.utils import flash_errors

from spaffnerds.music.models import Show

import datetime


blueprint = api.create_api_blueprint(
    'shows',
    Show,
    methods=['GET', 'POST', 'DELETE']
    )