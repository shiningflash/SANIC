from sanic import Sanic
from sanic.request import Request
from  sanic.response import text, json, HTTPResponse

app = Sanic(__name__)

@app.route('/')
async def hello(request):
    return json({
        'name': 'amirul',
        'status': 'inactive'
    })
    
@app.route('/app')
async def auth_token(request):
    return text(request.token)

@app.route('/response')
async def handler(request):
    return text("Done!", headers={
        "context-language": "en-US"
    })
    
@app.middleware('request')
async def middleware1(request):
    print('middleware_1')

@app.middleware('request')
async def middleware2(request):
    print('middleware_2')

@app.middleware('response')
async def middleware3(request, response):
    print('middleware_3')
    
@app.middleware('response')
async def middleware4(request, response):
    print('middleware_4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True, auto_reload=True)