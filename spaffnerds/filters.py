# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
import jinja2
from flask import Blueprint

import datetime

blueprint = Blueprint('filters', __name__)

# using the decorator
@jinja2.contextfilter
@blueprint.app_template_filter()
def datefilter(context, value, format='%Y/%m/%d'):
    """convert a datetime to a different format."""
    if not value:
        return None
    return value.strftime(format)
    