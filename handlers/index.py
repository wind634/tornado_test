import tornado.web

from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def prepare(self):
        pass
    
    def get(self):
        lst = "welcome you."
        self.render("index.html", info=lst)