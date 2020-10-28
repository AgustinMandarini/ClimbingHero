from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from climbinghero.models import Continent, Country, Province, Sector, Subsector, Route, User

class NewAreaCreationForm(FlaskForm):
	continent = SelectField('Continent', choices=[], default=1)
	country = SelectField('Country', choices=[])
	province = SelectField('Province', choices=[])
	submit = SubmitField('Nuevo Sector')
	submit = SubmitField('Nuevo Sub-sector')
	submit = SubmitField('Nueva Ruta')

class NewSector(FlaskForm):
	name = StringField('Nombre', 
						validators=[DataRequired(), Length(min=1, max=50)])
	descr = TextAreaField('Descripción', 
						validators=[DataRequired(), Length(min=2, max=1000)])
	getin = TextAreaField('Cómo llegar', 
						validators=[DataRequired(), Length(min=2, max=1000)])
	province_id = IntegerField('province_id')

class NewSubSector(FlaskForm):
	name = StringField('Nombre', 
						validators=[DataRequired(), Length(min=1, max=50)])
	descr = TextAreaField('Descripción', 
						validators=[DataRequired(), Length(min=2, max=1000)])
	getin = TextAreaField('Cómo llegar', 
						validators=[DataRequired(), Length(min=2, max=1000)])
	sector_id = IntegerField('sector_id')

class NewRoute(FlaskForm):
	name = StringField('Nombre', 
						validators=[DataRequired(), Length(min=1, max=50)])
	leng = IntegerField('Lenght')
	pitch = IntegerField('Number of pitches')
	grade = StringField('Grado de dificultad', validators=[Length(min=1, max=4)])
	style = StringField('Tipo/Estilo')
	descr = TextAreaField('Descripción', 
						validators=[DataRequired(), Length(min=2, max=1000)])
	equip = StringField('Equipo necesario')
	sector_id = IntegerField('sector_id')
	subsector_id = IntegerField('subsector_id')

