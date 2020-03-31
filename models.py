from peewee import *
from flask_login import UserMixin


database = SqliteDatabase("user.sqlite3")

class BaseModel(Model):

    class Meta:
        database = database

class User(BaseModel, UserMixin):
    login = CharField()
    password = CharField()

class Flux(BaseModel):
    lien = CharField()
    user = BigIntegerField()

def create_tables():
    with database:
        database.create_tables([User,Flux ])

def drop_tables():
    with database:
        database.drop_tables([User,Flux ])

    