# Flask/Sanic error cats (and dogs)

Extension that allows you to return error cats instead of regular error pages.

Extension uses:

- https://http.cat/
- https://httpstatusdogs.com/



## Usage

### Flask

```python
from error_cats import FlaskErrorCats
from flask import Flask

app = Flask(__name__)
FlaskErrorCats(app, status_codes=set(range(0, 600)), animal='dog')


@app.route('/<int:status_code>')
def status_code_view(status_code):
    return '', status_code


if __name__ == '__main__':
    app.run()

```


### Sanic

```python
from error_cats import SanicErrorCats
from sanic import Sanic
from sanic.response import json

app = Sanic()
SanicErrorCats(app, status_codes=set(range(0, 600)))


@app.route('/<status_code:int>')
async def status_code_view(request, status_code):
    return json('', status=status_code)


if __name__ == '__main__':
    app.run()
```

## Available parameters


| param | default | value |
|---|---|---|
| `app` | `None` (can be configured later) | Web application (Flask or Sanic) |
| `animal` | `cat` | Available values: `cat`, `dog` |
| `status_codes` | `400...599` | Container with status codes that should be translated into cats |
| `simple_html_template` | `...` | Simple python format string (html). Should contain `{status_cde}` (int) and `{image}` (url) |
