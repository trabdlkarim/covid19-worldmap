import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)


bp = Blueprint('page', __name__, url_prefix='/covidmap')

@bp.route('/about')
def about():
    return render_template('pages/about.html')

@bp.route('/terms')
def terms():
    return render_template('pages/terms.html')

@bp.route('/privacy')
def privacy():
    return render_template('pages/privacy.html')

@bp.route('/contribute')
def contribute():
    return render_template('pages/contribute.html')
