import multiprocessing

print(dir(multiprocessing))
print(multiprocessing.cpu_count())

import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop

from tornado.options import options, define


define("port", type=int, default=9001)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h1>hello world!</h1>")
        

urls = [
    (r"/", IndexHandler)
]

configs = dict(
    debug = True
)


class CustomApplication(tornado.web.Application):
    
    def __init__(self, configs, urls):
        settings = configs
        handlers = urls
        super(CustomApplication, self).__init__(handlers=handlers, **settings)
        
        
def create_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomApplication(configs, urls))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
app = create_app

if __name__ == "__main__":
    app()
    