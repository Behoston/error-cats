import abc

AVAILABLE_ERROR_ANIMALS = {
    'cat': 'https://http.cat/{}',
    'dog': 'https://httpstatusdogs.com/img/{}.jpg',
}

DEFAULT_ERROR_CODES = set(range(400, 600))

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{status_code}</title>
</head>
<body>
<img alt="{status_code}" src="{image}"/>
</body>
</html>
"""


class ErrorCats(metaclass=abc.ABCMeta):
    def __init__(self, app=None, animal='cat', status_codes=DEFAULT_ERROR_CODES, simply_html_template=TEMPLATE):
        """
        :param app: Web application
        :param animal: List of all available animal can be found in `error_cats.AVAILABLE_ERROR_ANIMALS`
        :param status_codes: all status codes that should be returned as cats
        :param simply_html_template: HTML template as format string. Available values: `image` (url) and `status_code`
        """
        self.animal = animal
        self.status_codes = status_codes
        self.template = simply_html_template
        if app is not None:
            self.init_app(app)

    @abc.abstractmethod
    def init_app(self, app):
        pass

    @abc.abstractmethod
    def process_response(self, *args, **kwargs):
        pass

    def generate_html(self, status_code):
        image = AVAILABLE_ERROR_ANIMALS[self.animal].format(status_code)
        return self.template.format(image=image, status_code=status_code)


class FlaskErrorCats(ErrorCats):
    def init_app(self, app):
        app.after_request(self.process_response)

    def process_response(self, response):
        if response.status_code in self.status_codes:
            html = self.generate_html(status_code=response.status_code)
            response.set_data(html)
            response.content_type = 'text/html'
        return response


class SanicErrorCats(ErrorCats):
    def init_app(self, app):
        app.middleware('response')(self.process_response)

    def process_response(self, request, response):
        if response.status in self.status_codes:
            html = self.generate_html(response.status)
            response.body = html.encode('utf-8')
            response.content_type = 'text/html'
