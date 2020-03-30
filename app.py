from flask import render_template, flash, redirect, url_for, Flask

from models import create_tables
from models import drop_tables

from forms import Inscription
from forms import Connexion

from models import User

import requests
# from user import User
import click


app = Flask(__name__)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# login_manager = LoginManager()

# login_manager.init_app(app)

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
    if form.validate_on_submit():
        form.populate_obj(user)
        user.save()
        flash('inscription effectuee')
        return redirect(url_for('index'))
    return render_template('inscription.html',form=form)



######"méthode avec session !!!!!!"########### à remplir
# @app.route('/login', methods=['GET', 'POST'])
# def login():

#     form = LoginForm()
#     if form.validate_on_submit():

#         login_user(user)

#         flask.flash('Logged in successfully.')

#         next = flask.request.args.get('next')

#         if not is_safe_url(next):
#             return flask.abort(400)

#         return flask.redirect(next or flask.url_for('index'))

#     return flask.render_template('login.html', form=form)


# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(somewhere)

# @app.cli.command()
# def fakedata():
#     from faker import Faker
#     from slugify import slugify
#     fake = Faker()
#     for pk in range(0, 42):
#         login = fake.user_name()
#         password = fake.color_name()
#         User.create(    
#                         login=login,
#                         password=password)

# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     form = -- RECUPERER LA FORM
#         login = form.login.data
#         mdp = form.password.data
#         existe = User.select().where(User.login == login).first()
#         if(existe == None):
#             utilisateur = User()
#             utilisateur.login = login.upper()
#             utilisateur.password = mdp
#             utilisateur.save()
#             return redirect(url_for('index'))
#         else:
#             flash("L'utilisateur existe déja")
#             return redirect(url_for('inscription'))
#     return render_template('inscription.html', form=form)    

# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     form = -- RECUPERER LA FORM
#         login = form.login.data
#         mdp = form.password.data
#         existe = User.select().where(User.login == login).first()
#         if(existe == None):
#             utilisateur = User()
#             utilisateur.login = login.upper()
#             utilisateur.password = mdp
#             utilisateur.save()
#             return redirect(url_for('index'))
#         else:
#             flash("L'utilisateur existe déja")
#             return redirect(url_for('inscription'))
#     return render_template('inscription.html', form=form)    

# @app.route('/flux', methods=['GET', 'POST'])
# @login_required
# def RegarderFlux():
#     linkFlux = request.args.get('linkFlux')
#     fluxparse = feedparser.parse(linkFlux)
#     element = feedparser.parse(linkFlux).entries
#     return render_template('RegarderFlux.html',fluxparse=fluxparse, element=element)