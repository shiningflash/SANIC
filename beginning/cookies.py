from sanic import Sanic
from sanic.request import Request
from sanic.response import text

import asyncio

app = Sanic(__name__)

@app.route('/')
async def home(request):
    test_cookie = request.cookies.get("test")
    print(__name__)
    print(app.name)
    app.add_task(notify_server_started_after_five_sec())
    return text(f'Text cookie is {test_cookie}')

@app.route('/cookie')
async def test(request):
    response = text("There is a cookie up in this response")
    response.cookies['test'] = "It works!"
    response.cookies['test']['domain'] = ".yummu-yummy-cookies.com"
    response.cookies['test']['httponly'] = True
    return response

async def notify_server_started_after_five_sec():
    await asyncio.sleep(5)
    print('Server started successfully')

if __name__ == '__main__':
    app.run()