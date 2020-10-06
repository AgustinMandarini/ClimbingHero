from flask import Flask, flash, redirect, request, render_template, session

# Configure app
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("map.html", title="Map", h2title="Wellcome to ClimbingHero!")

@app.route('/new_sector', methods = ['GET', 'POST'])
def new_sector():
    if request.method == 'POST':
        mapFeatures = request.get_json()
        print(mapFeatures)
        return redirect(url_for('home'))
    return render_template("map_edit.html", title="Map Edit", h2title="Use the map to add new routes!")
