from flask import Flask

from error_cats import FlaskErrorCats


def app_factory(cat_settings):
    app = Flask(__name__)
    FlaskErrorCats(app, **cat_settings)

    @app.route('/<int:status_code>')
    def status_code_view(status_code):
        return '', status_code
    app.test_client()
    return app
