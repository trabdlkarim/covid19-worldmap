#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:49:53 2020

@author: trabdlkarim
"""

import folium


def get_folium_map():
    return folium.Map(location=[34.223334,-82.461707],tiles='Stamen toner',
                      zoom_start=8)

def draw_circle(mp,x):
    folium.Circle(location=[x[0],x[1]],radius=float(x[2])*3,
                 color="red",
                 popup='confirmed cases:{}'.format(x[2])).add_to(mp)

def apply_df_map(df,mp):
    df = df[['Lat','Long_','Confirmed']]
    df = df.dropna()
    df.apply(lambda x:draw_circle(mp,x),axis=1)
    return mp._repr_html_()