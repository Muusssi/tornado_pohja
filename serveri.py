import tornado.ioloop
import tornado.web
import tornado.httpserver
import os
import sys
import json

import database as db

APP_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
STATIC_DIRECTORY = os.path.abspath(os.path.join(APP_DIRECTORY, 'static'))
TEMPLATES_DIRECTORY = os.path.abspath(os.path.join(APP_DIRECTORY, 'templates'))

def load_config_file(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

class Application(tornado.web.Application):
    def __init__(self, database):
        handlers = [
                (r"/", MainPageHandler),
                (r"/demo", DemoHandler),
            ]

        settings = dict(
                template_path=TEMPLATES_DIRECTORY,
                static_path=STATIC_DIRECTORY,
                debug=True,
            )
        self.database = database
        tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.database

class MainPageHandler(BaseHandler):
    def get(self):
        self.render('main_page.html')

class DemoHandler(BaseHandler):
    def get(self):
        self.render('processing_demo.html')


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        exit(1)
    config = load_config_file(sys.argv[1])
    application = Application(db.Database(config['database'], config['host'], config['user'], config['password']))
    httpserver = tornado.httpserver.HTTPServer(application)
    httpserver.listen(int(config['port']))
    print("Server listening port {}".format(config['port']))
    tornado.ioloop.IOLoop.current().start()


