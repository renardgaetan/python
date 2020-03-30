from flask import Flask
from models import create_tables
from models import drop_tables
import click


app = Flask(__name__)

@app.cli.command()
def initdb():
    """Create database"""
    create_tables()
    click.echo('Initialized the database')

@app.cli.command()
def dropdb():
    """Drop database tables"""
    drop_tables()
    click.echo('Dropped tables from database')


# @app.route('/flux', methods=['GET', 'POST'])
# @login_required
# def RegarderFlux():
#     linkFlux = request.args.get('linkFlux')
#     fluxparse = feedparser.parse(linkFlux)
#     element = feedparser.parse(linkFlux).entries
#     return render_template('RegarderFlux.html',fluxparse=fluxparse, element=element)