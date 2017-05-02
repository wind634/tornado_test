import tornado.web

from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    
    def get(self):
        lst = "welcome you."
        self.render("index.html", info=lst)