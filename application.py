from url import url

import tornado.web
import os


class Application(tornado.web.Application):
    def __init__(self, handlers, settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        
        # self.db =
