from sanic import Sanic
from sanic.request import Request
from sanic.response import text, HTTPResponse, json, redirect
from sanic.exceptions import SanicException

app = Sanic.get_app(
    'Hello World App',
    force_create=True
)


@app.get('/')
async def hello_world(request):
    return text('Hello World!')


@app.get('/tag/<tag>')
async def set_tag_name(request, tag):
    return json({
        'name': tag,
        'active_status': False
    }, status=201)

    
async def hello(request: Request) -> HTTPResponse:
    return text('Yayyy!!!!')

app.add_route(
    hello_world,
    '/api',
    methods=['GET', 'POST', 'PUT']
)

@app.route('/post')
async def show_post(request):
    url = app.url_for('set_tag_name', tag='amirul')
    return redirect(url)

@app.listener("before_server_start")
async def listener1(app, loop):
    print("before server start : Listener 1")
    
@app.listener("after_server_start")
async def listener2(app, loop):
    print("after server start : Listeneer 2")
    
@app.listener("before_server_stop")
async def listener3(app, loop):
    print("before server stop : Listener 3")
    
@app.listener("after_server_stop")
async def listener4(app, loop):
    print("after server stop : Listener 4")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True, auto_reload=True)