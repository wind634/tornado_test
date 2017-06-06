#!/usr/bin/env python
# coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

import sys

from application import Application

from tornado.options import define, options

from settings import settings
from url import url


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(url, settings))
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()


if __name__=="__main__":
    main()