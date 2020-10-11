import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configure app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa4d1c0d632b2e94366374fb1b7eb081f78292ec2300ad47a91184c5abe32cfd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from climbinghero import routes
