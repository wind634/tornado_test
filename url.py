#!/usr/bin/env python

from handlers.index import IndexHandler

url = [
    (r'/', IndexHandler),
    # (r'/query', QueryGene),

    ]
