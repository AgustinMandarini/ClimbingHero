import os
from climbinghero import app, db
from climbinghero.models import Continent, Country, Province, Sector, Subsector, Route, User
from climbinghero.forms import FirstRouteCreationForm
from flask import Flask, flash, redirect, request, render_template, session, url_for, jsonify
import json

@app.route('/home', methods = ['GET', 'POST'])
@app.route('/')
def home():

    form = FirstRouteCreationForm()
    form.continent.choices = [(continent.id, continent.name) for continent in Continent.query.all()]

    if request.method == "POST":
        country = Country.query.filter_by(id=form.country.data).first()

    sectorsArea = []
    sectors = Sector.query.all()
    for sector in sectors:
        sectorsArea.append(sector.coord)  

    return render_template("map.html", title="Map",\
    h2title="Encontra tu sector aca!", sectorsArea = sectorsArea, \
    form=form)

@app.route('/country/<continent>')
def country(continent):
    countries = Country.query.filter_by(continent_id=continent).all()

    countryArray = []

    for country in countries:
        countryObj = {}
        countryObj['id'] = country.id
        countryObj['name'] = country.name
        countryArray.append(countryObj)

    return jsonify({'countries' : countryArray})

@app.route('/province/<country>')
def province(country):
    provinces = Province.query.filter_by(country_id=country).all()

    provinceArray = []

    for province in provinces:
        provinceObj = {}
        provinceObj['id'] = province.id
        provinceObj['name'] = province.name
        provinceArray.append(provinceObj)

    return jsonify({'provinces' : provinceArray})

@app.route('/new_sector', methods = ['GET', 'POST'])
def new_sector():
    if request.method == "POST":
        mapFeatures = request.get_json()
        subsector = Subsector(area=mapFeatures)
        db.session.add(subsector)
        db.session.commit()
        # redirection to home is by AJAX call

    return render_template("map_edit.html", title="Map Edit", h2title="Use the map to add new routes!")
