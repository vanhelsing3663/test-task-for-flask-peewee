import random

from flask import request
from peewee import *

db = PostgresqlDatabase('postgres', host='localhost', port='5432', password='1234', user='postgres')


class Data(Model):
    id = BigAutoField(unique=True)
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'data'




