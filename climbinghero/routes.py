import os
from climbinghero import app, db
from climbinghero.models import JSONEncodedDict, Continent, Country, Province, Sector, Subsector, Route, User
from flask import Flask, flash, redirect, request, render_template, session, url_for
import json

@app.route('/home', methods = ['GET', 'POST'])
@app.route('/')
def home():
    sectorsArea = []
    countries = Country.query.all()
    sectors = Sector.query.all()
    for sector in sectors:
        sectorsArea.append(sector.coord)

    return render_template("map.html", title="Map",\
    h2title="Encontra tu sector aca!", sectorsArea = sectorsArea, \
    countries = countries)

@app.route('/new_sector', methods = ['GET', 'POST'])
def new_sector():
    if request.method == "POST":
        mapFeatures = request.get_json()
        subsector = Subsector(area=mapFeatures)
        db.session.add(subsector)
        db.session.commit()
        # redirection to home is by AJAX call

    return render_template("map_edit.html", title="Map Edit", h2title="Use the map to add new routes!")
