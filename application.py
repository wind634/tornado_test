import tornado.web
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from tornado.options import define, options


define("port", default=8888, help="run on th given port", type=int)
define("db_host", default="127.0.0.1", type=str)
define("db_user", default="root", type=str)
define("db_pwd", default="root", type=str)
define("db_name", default="testdb", type=str)
define("db_prot", default=3306, type=int)


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
