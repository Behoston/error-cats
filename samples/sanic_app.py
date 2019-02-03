from flask_error_cats import ErrorCats

from sanic import Sanic
from sanic.response import json

app = Sanic()
ErrorCats(app, status_codes=set(range(0, 600)))


@app.route('/<status_code:int>')
async def test(request, status_code):
    return json('', status=status_code)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
