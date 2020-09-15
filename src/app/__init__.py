#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from flask import Flask
from flask import (render_template, redirect, url_for)

from app.covid19 import dataset as ds
from app.covid19 import fmap
from app import page, dataframe

COVID_DATA_DIR = os.path.dirname(__file__)

def create_app(test_config=None):

    webapp = Flask(__name__, instance_relative_config=True)
    webapp.config.from_mapping(SECRET_KEY='vkSW7bv5fe',DATABASE=os.path.join(webapp.instance_path, 'app_db.sqlite'),)

    if test_config is None:
        webapp.config.from_pyfile('config.py', silent=True)
    else:
        webapp.config.from_mapping(test_config)


    try:
        os.makedirs(webapp.instance_path)
    except OSError:
        pass

    cdf = ds.get_top_infected_countries(n=20)
    pairs = [(country,confirmed) for country,confirmed in zip(cdf.index,cdf['Confirmed'])]

    covid19_df = ds.get_covid_df()


    fm = fmap.get_folium_map()

    html_map = fmap.apply_df_map(covid19_df,fm)

    @webapp.route('/covidmap/')
    def home():
        return render_template('home.html',c_table =cdf,wmap=html_map,pairs=pairs)

    @webapp.route('/')
    def index():
        return redirect(url_for('home'))

    webapp.register_blueprint(page.bp)
    webapp.register_blueprint(dataframe.bp)

    return webapp

