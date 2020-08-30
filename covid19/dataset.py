#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:35:44 2020

@author: trabdlkarim
"""

import pandas as pd


DATASETPATH = 'datasets/covid-19-dataset-1.csv'

def get_covid_df(did=1):
    path = 'datasets/covid-19-dataset-%i.csv' % did
    return pd.read_csv(path)

def get_top_infected_countries(did=1,n=10):
    dataset = get_covid_df(did)
    gby_df = dataset.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered','Active']]
    cdf = gby_df.nlargest(n,'Confirmed')[['Confirmed']]
    return cdf
