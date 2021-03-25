from peewee import *
from sanic import Sanic
from sanic.response import text

app = Sanic(
    'database_app',   
)

db = PostgresqlDatabase(
    'db',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost'
)

class BaseModel(Model):
    class Meta:
        database = db
        
class User(BaseModel):
    name = CharField()
    username = CharField()
        
    
@app.route('/')
async def hello(request):
    return text('connected')

conn = db.connection()
db.create_tables([User])

if __name__ == '__main__':
    app.run()