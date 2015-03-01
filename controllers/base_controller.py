import bottle, authentication_controller, profile_controller, os
from bottle import get, view, post, error, route

@error(404)
def error404(error):
	return 'Nothing here, sorry'

@route('/styles/<path:path>')
def send_styles(path):
	stylesRoot = os.getcwd() + '/styles'
	return bottle.static_file(path, root=stylesRoot)

@route('/scripts/<path:path>')
def send_scripts(path):
	scriptsRoot = os.getcwd() + '/scripts'
	return bottle.static_file(path, root=scriptsRoot)

@route('/images/<path:path>')
def send_images(path):
	imagesRoot = os.getcwd() + '/images'
	return bottle.static_file(path, root=imagesRoot)