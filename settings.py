import os
from tornado.options import define

base_dir = os.path.dirname(__file__)

define("port", default=8888, help="run on th given port", type=int)
define("db_host", default="127.0.0.1", type=str)
define("db_user", default="root", type=str)
define("db_pwd", default="root", type=str)
define("db_name", default="testdb", type=str)
define("db_prot", default=3306, type=int)


settings = dict(
    template_path=os.path.join(base_dir, "templates"),
    static_path=os.path.join(base_dir, "static"),
    debug=True,
    title="abcde",
)
