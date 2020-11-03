import os
from climbinghero import app, db
from climbinghero.models import Continent, Country, Province, Sector, Subsector, Route, User, Grades
from climbinghero.forms import NewAreaCreationForm, NewSector, NewSubSector, NewRoute
from flask import Flask, flash, redirect, request, render_template, session, url_for, jsonify
import json



@app.route('/home', methods = ['GET', 'POST'])
@app.route('/')
def home():

    print("redireccion a home, antes que nada")
    form = NewAreaCreationForm()
    form.continent.choices = [(continent.id, continent.name) for continent in Continent.query.all()]

    if request.method == "POST":
        print("redireccion a home, justo despues de POST")
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

    if request.method == "GET":

        data = json.loads(new_area_data)
        if data['submit'] == 'Nuevo Sector':
            form = NewSector()

        elif data['submit'] == 'Nuevo Sub-sector':
            form = NewSubSector()

        elif data['submit'] == 'Nueva Ruta':
            form =  NewRoute()
            form.grade.choices = [(grade.id, grade.french) for grade in Grades.query.all()]

        return render_template("map_new.html", title="New Area", 
                            h2title="Use the map to add new routes!", 
                            data=data, form=form)
  
    if request.method == "POST":
        ajaxpost = request.get_json()
        province_id = int(ajaxpost["parent"])
        sector = Sector(name=ajaxpost["name"], descr=ajaxpost["descr"], getin=ajaxpost["getin"], \
                        province_id=province_id, coord=ajaxpost["mapfeatures"])
        db.session.add(sector)
        db.session.commit()
        
        return redirect("/home")
        # Redirection to home is also in AJAX call, in map_edit.js
        # For a reason i dont know, redirection needs to be called in both
        # here (new_place route) and in AJAX POST request.
        # Involved in this bug is also the fact that two GET requests are
        # being sent to home route, one of wich does not redirect, the
        # other one does.
    
