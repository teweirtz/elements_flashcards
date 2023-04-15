from peewee import *

db = PostgresqlDatabase('elements', user='postgres', password='',host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db
class Elements(BaseModel):
    name = CharField()
    abbreviation = CharField()
