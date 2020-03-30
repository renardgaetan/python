from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import PasswordInput
from feedparser import *

class ajouterFlux(FlaskForm):
    lien = StringField('Lien du flux', validators=[DataRequired()])
    pass

class Inscription(FlaskForm):
    login = StringField('login ', validators=[DataRequired(), Length(min=4, max=15)])
    password = StringField('password ', widget=PasswordInput(hide_value=True))
    pass

class Connexion(FlaskForm):
    login = StringField('login ', validators=[DataRequired(), Length(min=4, max=15)])
    password = StringField('password ', widget=PasswordInput(hide_value=True))
    pass


