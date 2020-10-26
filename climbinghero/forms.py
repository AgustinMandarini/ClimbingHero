from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from climbinghero.models import Continent, Country, Province, Sector, Subsector, Route, User

class FirstRouteCreationForm(FlaskForm):
	continent = SelectField('Continent', choices=[])
	country = SelectField('Country', choices=[])
	province = SelectField('Province', choices=[])