import time
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def ok_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, headers)
    ret = [b'{"message": "OK"}\n']

    time.sleep(5)

    return ret


if __name__ == "__main__":
    httpd = make_server('', 5000, ok_app)
    print("Serving on 5000...")
    httpd.serve_forever()