from url import url

import tornado.web
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from tornado.options import options

engine = create_engine(
            'mysql+pymysql://%s:%s@%s:%d/%s' % (
                options.db_user,
                options.db_pwd,
                options.db_host,
                options.db_port,
                options.db_name,
            ),
            encoding='utf-8',
            echo=False,
            pool_size=100,
            pool_recycle=7200,
            connect_args={'charset':'utf8'},
        )


class Application(tornado.web.Application):
    def __init__(self, handlers, settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        
        self.db = scoped_session(sessionmaker(bind=engine, autocommit=False, expire_on_commit=False,
                               autoflush=True))
