import bottle, authentication_controller
from bottle import get, view, post, error

@error(404)
def error404(error):
    return 'Nothing here, sorry'