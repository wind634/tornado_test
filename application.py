from url import url

import tornado.web
import os


class Application(tornado.web.Application):
    def __init__(self):
        handlers = url
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

        tornado.web.Application.__init__(self, handlers, settings)
        
        # self.db =
