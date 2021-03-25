from peewee import CharField, DateTimeField, PostgresqlDatabase, Model
import datetime
from sanic import Sanic
from sanic_crud import generate_crud

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
    create_datetime = DateTimeField(default=datetime.datetime.now)

db.create_tables([Person])

app = Sanic(__name__)
generate_crud(app, [Person])
app.run(host="0.0.0.0", port=8000, debug=True)