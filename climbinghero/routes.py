import os
from climbinghero import app, db
from climbinghero.models import Continent, Country, Province, Sector, Subsector, Route, User
from climbinghero.forms import NewAreaCreationForm, NewSector, NewSubSector, NewRoute
from flask import Flask, flash, redirect, request, render_template, session, url_for, jsonify
import json


@app.route('/home', methods = ['GET', 'POST'])
@app.route('/')
def home():

    form = NewAreaCreationForm()
    form.continent.choices = [(continent.id, continent.name) for continent in Continent.query.all()]

    if request.method == "POST":
        continent = Continent.query.filter_by(id=form.continent.data).first()
        country = Country.query.filter_by(id=form.country.data).first()
        province = Province.query.filter_by(id=form.province.data).first()
        submit = (request.form.to_dict())['submit']

        if not country or not province:
            return '<h1>ERROR!! Para crear una nueva area es necesario que especifiques un continente, pais y provincia.</h1>'

        new_area_data = json.dumps({'continent': continent.name, 'continent_id': continent.id, 
                                    'country': country.name, 'country_id': country.id,
                                    'province': province.name, 'province_id': province.id, 
                                    'submit': submit})

        return redirect(url_for('new_place', new_area_data=new_area_data))

    #'<h1>Continent : {}, Country: {}, Province: {}</h1>'.format(continent.name, country.name, province.name)

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

@app.route('/new_place/<new_area_data>', methods = ['GET', 'POST'])
def new_place(new_area_data):

    data = json.loads(new_area_data)
    print(data['submit'])

    if data['submit'] == 'Nuevo Sector':
        form = NewSector()    
    elif data['submit'] == 'Nuevo Sub-sector':
        form = NewSubSector()
    elif data['submit'] == 'Nueva Ruta':
        form =  NewRoute()

    if request.method == "POST":
        mapFeatures = request.get_json()
        subsector = Subsector(area=mapFeatures)
        db.session.add(subsector)
        db.session.commit()
        # redirection to home is by AJAX call                                               								

    return render_template("map_new.html", title="New Area", h2title="Use the map to add new routes!", data=data, form=form)
