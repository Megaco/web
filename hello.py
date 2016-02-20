#!/usr/bin/python

from urllib.parse import parse_qs

def application(environ, start_response):
    params = parse_qs(environ["QUERY_STRING"])

    body = ""
    for k in sorted(params):
        body += k + "="+ "".join(params[k]) + "\n"
        # body += "\n  ".join(params[k])


    start_response('200 OK', [('Content-Type', 'text/plain')])

    return [body.encode('utf-8')]