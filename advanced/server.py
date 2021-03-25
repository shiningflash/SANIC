from sanic import Sanic
from sanic.request import Request
from sanic.response import text
from sanic.views import HTTPMethodView

app = Sanic(__name__)

class FooBar(HTTPMethodView):
    
    async def get(self, request, name):
        return text(f'Hello! {name}')
    
    async def post(self, request):
        pass
    
    async def put(self, request):
        pass
    
app.add_route(FooBar.as_view(), '/foobar/<name>')

if __name__ == '__main__':
    app.run(debug=True, auto_reload=True) 