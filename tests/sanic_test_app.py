from sanic import Sanic
from sanic.response import json

from error_cats import SanicErrorCats


def app_factory(cat_settings):
    app = Sanic()
    SanicErrorCats(app, **cat_settings)

    @app.route('/<status_code:int>')
    async def status_code_view(request, status_code):
        return json('', status=status_code)

    return app
