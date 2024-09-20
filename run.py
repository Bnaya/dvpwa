import sys
import logging

import aiohttp_jinja2
# from aiohttp.web import run_app
import aiohttp
# from sqli.app import init as init_app

log = logging.getLogger(__name__)

aiohttp_jinja2.template('tmpl.jinja2')

@aiohttp_jinja2.template('tmpl.jinja2')
def handler(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(sys.argv[1:])

    host = app['config']['app']['host']
    port = app['config']['app']['port']
    log.info(f'App is listening at http://{host}:{port}')
    aiohttp.web.run_app(app, host=host, port=port)
