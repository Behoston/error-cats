from .sanic_test_app import app_factory


def test_sanic_cat():
    client = app_factory(cat_settings={}).test_client
    _, response = client.get('/400')
    assert b'https://http.cat/400' in response.body


def test_sanic_cat_only_for_given_status_codes():
    app = app_factory(cat_settings={'status_codes': {500}, })
    client = app.test_client

    _, response = client.get('/500')
    assert b'https://http.cat/500' in response.body

    _, response = client.get('/200')
    assert b'https://http.cat' not in response.body


def test_sanic_dog():
    client = app_factory(cat_settings={
        'animal': 'dog',
    }).test_client
    _, response = client.get('/400')
    assert b'https://httpstatusdogs.com/img/400.jpg' in response.body


def test_sanic_custom_simple_template():
    client = app_factory(cat_settings={
        'simple_html_template': '<title>example.com - {status_code}</title>',
    }).test_client
    _, response = client.get('/400')
    assert b'<title>example.com - 400</title>' == response.body
