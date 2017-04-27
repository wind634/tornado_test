import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    
    def get(self):
        lst = "welcome you."
        self.render("index.html", info=lst)