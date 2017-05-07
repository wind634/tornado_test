import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options

define('port', type=int, default=9000)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h1>hello tony</h1>")

urls = [
    (r"/", IndexHandler)
]

configs = dict(
    debug = True
)


class CustomAppliaction(tornado.web.Application):
    def __init__(self, urls, configs):
        handlers = urls
        super(CustomAppliaction, self).__init__(handlers=handlers, **configs)


def create_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomAppliaction(urls))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
app = create_app()

if __name__ == "__main__":
    app()