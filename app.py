from flask import render_template, flash, redirect, url_for, request, Flask

from models import create_tables
from models import drop_tables

from forms import Inscription
from forms import Connexion
from forms import AjouterFlux

from models import User
from models import Flux

from flask_login import login_user, current_user, login_required, LoginManager, logout_user


import requests

# from user import User
import click

import feedparser


app = Flask(__name__)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(id=user_id)

#créer table
@app.cli.command()
def initdb():
    """Create database"""
    create_tables()
    click.echo('Initialized the database')

#drop table
@app.cli.command()
def dropdb():
    """Drop database tables"""
    drop_tables()
    click.echo('Dropped tables from database')

@app.route('/')
def index():
    return render_template('index.html')
    
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

#inscription
@app.route('/inscription', methods=['GET', 'POST', ])
def user_create():
    user = User()
    form = Inscription()
    login = form.login.data
    mdp = form.password.data
    existe = User.select().where(User.login == login).first()
    if(existe == None):
        if form.validate_on_submit():
            form.populate_obj(user)
            user.save()
            flash('inscription effectuee')
            return redirect(url_for('index'))
        return render_template('inscription.html',form=form)
    return render_template('inscription.html',form=form)

@app.route('/connexion', methods=['GET', 'POST', ])
def connexion():
    form = Connexion() 
    if form.validate_on_submit():
        loginConnecte = form.login.data
        mdpConnecte = form.password.data
        user = User.select().where((User.login == loginConnecte) & (User.password == mdpConnecte)).first()
        if (user == None):
            print("Identifiants incorrect")
        else:
            login_user(user)
            current_user.id = user.id
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    list_flux=[]
    list_flux_user = Flux.select().where((Flux.user == current_user.id))
    for i in list_flux_user:
        fluxparse = feedparser.parse(i.lien)
        list_flux.append(fluxparse)

    return render_template('dashboard.html', list_flux_user=list_flux_user, list_flux=list_flux)

@app.route('/deconnexion')
@login_required
def deconnexion():
    logout_user()
    return redirect(url_for('index'))

@app.route('/ajouterFlux', methods=['GET', 'POST', ])
@login_required
def ajouterFlux():
    form = AjouterFlux()
    if form.validate_on_submit():
        fluxExistant = Flux.select().where((Flux.lien == form.lien.data) & (Flux.user == current_user.id)).first()
        if(fluxExistant == None):
            flux = Flux()
            flux.user = current_user.id
            flux.lien = form.lien.data
            flux.save()
            return redirect(url_for('dashboard'))   
        else:
            return redirect(url_for('ajouterFlux'))
    return render_template('ajouterFlux.html',form=form)

@app.route('/regarderFlux', methods=['GET', 'POST'])
@login_required
def regarderFlux():
    lienFlux = request.args.get('lienFlux')
    fluxparse = feedparser.parse(lienFlux)
    print(fluxparse)
    element = fluxparse.entries
    print(element)
    return render_template('regarderFlux.html',fluxparse=fluxparse,element=element)

@app.route('/supprimerFlux', methods=['GET','POST'])
@login_required
def supprimerFlux():
    flux_idUser = request.args.get('flux_idUser')
    flux_lien = request.args.get('flux_lien')
    requete = Flux.delete().where((Flux.user == flux_idUser) & (Flux.lien == flux_lien))
    requete.execute()
    return redirect(url_for('dashboard'))