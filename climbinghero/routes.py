import os
from climbinghero import app, db
from climbinghero.models import JSONEncodedDict, Sectors
from flask import Flask, flash, redirect, request, render_template, session, url_for
import json

@app.route('/home')
@app.route('/')
def home():
    sectorsArea = []
    sectors_list = Sectors.query.all()
    for sector in sectors_list:
        sectorsArea.append(sector.area)

    print(sectorsArea)
    print(type(sectorsArea))
    print(type(sectorsArea[0]))

    return render_template("map.html", title="Map", h2title="Wellcome to ClimbingHero!", sectorsArea = sectorsArea)

@app.route('/new_sector', methods = ['GET', 'POST'])
def new_sector():
    if request.method == "POST":
        mapFeatures = request.get_json()
        sector = Sectors(area=mapFeatures)
        db.session.add(sector)
        db.session.commit()
        # redirection to home is by AJAX call

    return render_template("map_edit.html", title="Map Edit", h2title="Use the map to add new routes!")
