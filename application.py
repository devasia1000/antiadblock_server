def application(environ, start_response):

    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return ["Hello!!!"]

    ### This app works, remember to ZIP the app first