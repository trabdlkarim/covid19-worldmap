#!/usr/bin/env python

from flask import (Blueprint, render_template, url_for,redirect)

from app.covid19 import dataset as ds
from app.covid19 import fmap

bp = Blueprint('dataset', __name__, url_prefix='/covidmap/dataset')

@bp.route('/<int:dsid>')
def data(dsid=1):
    cdf = ds.get_top_infected_countries(dsid,15)
    pairs = [(country,confirmed) for country,confirmed in zip(cdf.index,cdf['Confirmed'])]

    covid19_df = ds.get_covid_df(dsid)


    fm = fmap.get_folium_map()

    html_map = fmap.apply_df_map(covid19_df,fm)

    return render_template('data.html',c_table =cdf,wmap=html_map,pairs=pairs,ds=dsid)

@bp.route('/')
def default():
    return redirect(url_for('dataset.data',dsid=1))
