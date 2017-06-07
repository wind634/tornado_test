import tornado.web

from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def prepare(self):
        pass
    
    def get(self):
        sql = ""
        self.db.excute(sql)
        self.db.commit()
        self.db.close()
        lst = "welcome you."
        self.render("index.html", info=lst)