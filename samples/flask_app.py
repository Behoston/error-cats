from flask import Flask

from flask_error_cats import ErrorCats

app = Flask(__name__)
ErrorCats(app, status_codes=set(range(0, 600)), animal='dog')


@app.route('/<int:status_code>')
def status_code_view(status_code):
    return '', status_code


if __name__ == '__main__':
    app.run()
