import os

from sanic import Sanic
from sanic.response import json, html, text

app = Sanic("My Hello, world app")

app.static('/static', './static')

@app.route('/')
async def test(request):
    template = open(os.getcwd() + "/templates/index.html")
    return html(template.read())

if __name__ == '__main__':
    app.run()
