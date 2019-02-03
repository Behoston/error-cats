from .flask_test_app import app_factory


def test_flask_cat():
    client = app_factory(cat_settings={}).test_client()
    response = client.get('/400')
    assert b'https://http.cat/400' in response.data


def test_flask_cat_only_for_given_status_codes():
    client = app_factory(cat_settings={
        'status_codes': {500},
    }).test_client()

    response = client.get('/500')
    assert b'https://http.cat/500' in response.data

    response = client.get('/200')
    assert b'https://http.cat' not in response.data


def test_flask_dog():
    client = app_factory(cat_settings={
        'animal': 'dog',
    }).test_client()
    response = client.get('/400')
    assert b'https://httpstatusdogs.com/img/400.jpg' in response.data


def test_flask_custom_simple_template():
    client = app_factory(cat_settings={
        'simple_html_template': '<title>example.com - {status_code}</title>',
    }).test_client()
    response = client.get('/400')
    assert b'<title>example.com - 400</title>' == response.data
