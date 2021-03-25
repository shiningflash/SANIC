import os
import json
import datetime
from sanic import Sanic
from sanic.response import text, json
from peewee import CharField, DateTimeField, PostgresqlDatabase, Model

db = PostgresqlDatabase(
    'db',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost'
)

class BaseModel(Model):
    class Meta:
        database = db
        
class Person(BaseModel):
    name = CharField()
    email = CharField()
    registered_at = DateTimeField(default=datetime.datetime.now(), null=True)
    
db.create_tables([Person])

app = Sanic(__name__)

def object_to_string(person):
    res = "["
    for i in range(len(person)):
        res += "{'name' : '" + person[i].name + "', "
        res += "'email' : '" + person[i].email + "'} "
        if i < len(person)-1:
            res += ","
    res += "]"
    return res

@app.route('/')
def home(request):
    person = Person.select().order_by(Person.name)
    # object to string -> then, string to json
    person_json = eval(object_to_string(person))
    return json(person_json)

app.run(host='0.0.0.0', port=8000, debug=True)

