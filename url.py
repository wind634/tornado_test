#!/usr/bin/env python

from handler.index import IndexHandler

url = [
    (r'/', IndexHandler),
    # (r'/query', QueryGene),

    ]
