from django.contrib.auth.models import User
from Sudakaweb.models import  Usuario
#from MP.forms import *



def datos_globales(request):
	if not request.user.is_anonymous():
		usuario = Usuario.objects.filter(user = request.user)
		if len(usuario) == 1:
			nombre = usuario[0].usuarioNombre
			if not 'ROL_USUARIO' in request.session:
				request.session['ROL_USUARIO'] = usuario[0].usuarioRol

			dict = {
				'NOMBRE_USUARIO':usuario[0].user.username,
				'NOMBRE_COMPLETO':nombre+" "+usuario[0].usuarioApellido,
				'ROL_USUARIO':request.session['ROL_USUARIO']
			}
		else:
			dict = {
				'NOMBRE_USUARIO':"Administrador",
				'NOMBRE_COMPLETO':"Administrador",
				'ROL_USUARIO':"Administrador"
			}
		return dict
	return {}

