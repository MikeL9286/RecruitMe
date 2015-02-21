import bottle, authentication_controller, os
from bottle import get, view, post, error, route

@error(404)
def error404(error):
	return 'Nothing here, sorry'

@route('/static/<path:path>')
def send_static(path):
	staticRoot = os.getcwd() + '/static'
	return bottle.static_file(path, root=staticRoot)