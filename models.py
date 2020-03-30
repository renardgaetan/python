from peewee import *

database = SqliteDatabase("user.sqlite3")

class BaseModel(Model):

    class Meta:
        database = database

class User(BaseModel):
    login = CharField()
    password = CharField()



def create_tables():
    with database:
        database.create_tables([User, ])

def drop_tables():
    with database:
        database.drop_tables([User, ])

    