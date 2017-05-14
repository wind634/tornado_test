import json
from urllib.parse import urlencode

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.httpclient
import tornado.gen

from tornado.options import define, options
from tornado.web import url, URLSpec

define('port', type=int, default=9000)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h1>hello tonyss</h1>")


class ProductHandler(tornado.web.RequestHandler):
    def get(self, price):
        self.write("<h1>the price of the product is %d</h1>" % int(price))
        
                
class PersonHandler(tornado.web.RequestHandler):
    def get(self, truename):
        self.write("<h1>the truename of the person is %s</h1>" % truename)

db = "mysql"


class StudentHandler(tornado.web.RequestHandler):
    
    def initialize(self, db):
        self.db = db
        
    def get(self, truename, age, height):
        self.write("<h1>姓名:%s,年龄:%d,身高:%d.</h1>" % (truename, int(age), int(height)))
        self.write("<br>")
        self.write(self.reverse_url("student", truename,age,height))
        
        
class TestHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write_error(404)


class Test2Handler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(404)


class Test3Handler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(404)


class Test4Handler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(status_code=404, log_message="test", reason="no page...`")
    

class ErrorHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<h1>404 no page</h1>')


class ReHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('http://www.baidu.com')

        
class ShowjsonHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_header()
        data = {}
        self.write(json.dumps(data))


class AsyncHandler(tornado.web.RequestHandler):
    
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        url = "http://www.baidu.com"
        # http_client = tornado.httpclient.HTTPClient()
        # response = http_client.fetch(url)
        # self.write(response.body)


class StudentHandler(tornado.web.RequestHandler):
    
    def get(self, *args, **kwargs):
        truename = self.get_argument("truename", "")
        num = self.get_argument("num", 0)
        age = self.get_argument("age", 0)
        height = self.get_argument("height", 0)
        self.write("get...")
        self.write("姓名:%s, 学号:%s, 年龄:%s, 身高:%s" % (truename, int(num), int(age), int(height)))
        
    def post(self, *args, **kwargs):
        truename = self.get_argument("truename", "")
        num = self.get_argument("num", 0)
        age = self.get_argument("age", 0)
        height = self.get_argument("height", 0)
        self.write("post...")
        self.write("姓名:%s, 学号:%s, 年龄:%s, 身高:%s" % (truename, int(num), int(age), int(height)))


class Async13Handler(tornado.web.RequestHandler):
    
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url="http://127.0.0.1:9000/stu"
        query = dict(
            truename="李四22",
            age=20,
            num=2,
            height=100,
        )
        http_client = tornado.httpclient.AsyncHTTPClient()
        request = tornado.httpclient.HTTPRequest(url, method="POST", body=urlencode(query))
        response = yield http_client.fetch(request)
        self.write(response.body)
        self.finish()
        
        # response = yield http_client.fetch(url + '?' + urlencode(query))
        # self.write(response.body)
        # self.finish()


class Async14Handler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = "http://127.0.0.1:9000/stu"
        query = dict(
            truename="李四qq",
            age=20,
            num=2,
            height=100,
        )
        http_client = tornado.httpclient.AsyncHTTPClient()
        request = tornado.httpclient.HTTPRequest(url, method="POST", body=urlencode(query))
        response = yield tornado.gen.Task(http_client.fetch, request)
        self.write(response.body)
        self.finish()


class Async15Handler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = "http://127.0.0.1:9000/stu"
        query_list = [
            dict(
                truename="李四11",
                age=20,
                num=2,
                height=100,
            ),
            dict(
                truename="李四222",
                age=20,
                num=2,
                height=100,
            ),
            dict(
                truename="李四333",
                age=20,
                num=2,
                height=100,
            ),
            dict(
                truename="李四444",
                age=20,
                num=2,
                height=100,
            ),
        ]
        http_client = tornado.httpclient.AsyncHTTPClient()
        # responses = yield [
        #     http_client.fetch(
        #         tornado.httpclient.HTTPRequest(url, method="POST", body=urlencode(query))
        #     )
        #     for query in query_list]

        responses = yield {
                tornado.httpclient.HTTPRequest(url, method="POST", body=urlencode(query))
                for query in query_list
        }
        for resp in responses:
            self.write(resp.body)
        self.finish()
        

urls = [
    (r"/", IndexHandler),
    (r"/index", IndexHandler),
    (r"/product1/(\d+)", ProductHandler),
    (r"/product2/([0-9]+)", ProductHandler),
    (r"/person1/(\w+)", PersonHandler),
    (r"/person2/([a-zA-Z]+)", PersonHandler),
    (r"/person3/(.*)", PersonHandler),
    url(r"/student1/    (?P<truename>.*)/(?P<age>\d+)/(?P<height>\d+)", StudentHandler, dict(db=db), name="student"),
    
    (r"/test1", TestHandler),
    (r"/test2", Test2Handler),
    (r"/test3", Test3Handler),
    (r"/test4", Test4Handler),


    (r"/bd", ReHandler),
    
    (r"/stu", StudentHandler),
    
    (r"/test13", Async13Handler),
    
    (r"/test14", Async14Handler),
    
    (r"/test15", Async15Handler),
    
    (r"/.*", ErrorHandler),
]

configs = dict(
    debug=True
)


class CustomAppliaction(tornado.web.Application):
    def __init__(self, urls, configs):
        handlers = urls
        super(CustomAppliaction, self).__init__(handlers=handlers, **configs)


def create_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomAppliaction(urls, configs))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
app = create_app()

if __name__ == "__main__":
    app()