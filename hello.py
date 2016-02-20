
def application(environ, start_response):
    params = environ["QUERY_STRING"].split("&")
    body = "\n".join(params)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [body.encode('utf-8')]