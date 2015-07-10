# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from Sudakaweb.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import *


class Home(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHome(self,request):
		context= {'pelicula':''}
		return render(request, 'Sudakaweb/home.html',context)

class inicio(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarInicio(self,request):
		return render(request, 'Sudakaweb/index.html',{})				

class nosotros(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarNosotros(self,request):
		return render(request, 'Sudakaweb/Nosotros.html',{})				

class catalogo(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarCatalogo(self,request):
		return render(request, 'Sudakaweb/Catalogo.html',{})				

class contacto(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarContacto(self,request):
		return render(request, 'Sudakaweb/Contacto.html',{})				

class registro(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarRegistro(self,request):
		form = UsuarioForm(request.POST or None)
		form2 = UserForm(request.POST or None)
		if request.method=='POST':
			if request.POST['password'] == request.POST["repite_contrasena"]:
				if form.is_valid() and form2.is_valid():
					usuario = form.save()
					user = form2.save()
					user.set_password(user.password)
					user.save()
					usuario.user = user
					usuario.save()
					messages.success(request,'Se ha registrado exitosamente.')
					return HttpResponseRedirect("/index")
				else:					
					if "usuarioCorreo" in form.errors:
						messages.error(request, "Debe ingresar un correo válido")
					if "usuarioTelefono" in form.errors:
						messages.error(request, "Debe ingresar un teléfono válido")
			else:
				messages.error(request,'Las contraseñas ingresadas no coinciden')
		ctx = {'UsuarioForm':form, 'UserForm':form2}
		return render(request, 'Sudakaweb/RegistroCliente.html',ctx)

class administradorInicio(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorInicio(self,request):
		return render(request, 'Sudakaweb/AdministradorInicio.html',{})

def logout_view(request):
    """
    Cierra la sesion de un usuario y lo redirecciona al home
    """
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
	if not request.method == 'POST': #Solicitud a la pagina por un formulario
		if not request.user.is_anonymous():
			return HttpResponseRedirect('/')
		return render(request, 'Sudakaweb/login.html',{})
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:					
				login(request, user)
				usuario= Usuario.objects.filter(user=user)
				if len(usuario)==1:
					messages.success(request,'Bienvenido ' + usuario[0].usuarioNombre)
				else:
					messages.success(request,'Bienvenido Administrador')
				return HttpResponseRedirect('/')
		messages.error(request,'Usuario o contrasena incorrectos')
		return render(request, 'Sudakaweb/login.html',{})

#Menu Material
class administradorVerMateriales(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorMateriales(self,request):
		material = Material.objects.exclude(materialSubTipo= 'Producto Terminado') # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'materiales':material} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerMateriales.html',ctx)

class administradorIngresarMaterial(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def ingresarAdministradorMaterial(self,request):
		return render(request, 'Sudakaweb/AdministradorIngresarMaterial.html',{})

class administradorEditarMaterial(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorMaterial(self,request,id):
		material = Material.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = MaterialForm(request.POST, instance=material)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente el material.')
				return HttpResponseRedirect("/AdministradorVerMateriales")
			else:
				ctx={'MaterialForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/AdministradorEditarMaterial.html',ctx)
		else:
			form = MaterialForm(instance=material)
			ctx={'MaterialForm':form,'id':id}
			return render(request, 'Sudakaweb/AdministradorEditarMaterial.html',ctx)

class administradorEliminarMaterial(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorMaterial(self,request,id):
		material = Material.objects.get(pk=id)
		tipo = material.materialSubTipo
		material.delete()
		if tipo == 'Producto Terminado':
			messages.success(request, "Se ha eliminado el producto.")
			return HttpResponseRedirect("/AdministradorVerProductos")
		else:
			messages.success(request, "Se ha eliminado el material.")
			return HttpResponseRedirect("/AdministradorVerMateriales")	

class administradorNuevoMaterial(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorMaterial(self,request):
		form= MaterialForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				material1= form.save()
				for x in request.POST['str_materiales'][:-1].split(';'):
					data=x.split(',')
					material2= Material.objects.get(pk=int(data[0]))
					comp= Composicion(material1= material1,material2= material2, composicionCantidad= int(data[1]))
					comp.save()
				messages.success(request,'Se ha ingresado correctamente el material.')
				return HttpResponseRedirect("/AdministradorVerMateriales")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= {'MaterialForm':form, "materiales": Material.objects.all() }
		return render(request, 'Sudakaweb/AdministradorNuevoMaterial.html',ctx)


#Menu Producto
class administradorVerProductos(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorProductos(self,request):
		material = Material.objects.filter(materialSubTipo= 'Producto Terminado') # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'materiales':material} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerProductos.html',ctx)

class administradorEditarProducto(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorProducto(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarProducto.html',{})

class administradorNuevoProducto(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorProducto(self,request):
		form= ProductoForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid() and request.POST['str_materiales'] != "":
				material= form.save()
				material.materialTipo= 'Elaborado'
				material.materialSubTipo= 'Producto Terminado'
				material.materialUnidadMedida= 'botellas'
				material.save()
				for x in request.POST['str_materiales'][:-1].split(';'):
					data=x.split(',')
					material2= Material.objects.get(pk=int(data[0]))
					comp= Composicion(material1= material,material2= material2, composicionCantidad= int(data[1]))
					comp.save()
				messages.success(request,'Se ha ingresado correctamente el material.')
				return HttpResponseRedirect("/AdministradorVerProductos")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= {'ProductoForm':form, "materiales": Material.objects.all() }
		return render(request, 'Sudakaweb/AdministradorNuevoProducto.html',ctx)

#Menu Cliente
class administradorVerClientes(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorClientes(self,request):
		cliente = Usuario.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'clientes':cliente} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerUsuarios.html',ctx)

class administradorEditarCliente(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorCliente(self,request,id):
		cliente = Usuario.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = UsuarioForm(request.POST, instance=cliente)
			form2 = UserForm(request.POST, instance= cliente.user)
			if request.POST['password'] == request.POST["repite_contrasena"]:
				if form.is_valid() and not "username" in form2.errors:
					form.save()
					if not "password" in form2.cleaned_data:
						cliente.user.username=form2.cleaned_data["username"]
						cliente.user.save()
					else:
						form2.save()
						cliente.user.set_password(cliente.user.password)
						cliente.user.save()
					messages.success(request,'El cliente ha sido modificado correctamente.')
					return HttpResponseRedirect("/AdministradorVerUsuarios")
				else:
					
					messages.success(request, "-"+str(form2.cleaned_data))
					ctx={'UsuarioForm':form,'id':id, 'UserForm':form2}
					messages.error(request,'Debe llenar correctamente todos los campos disponibles.'+ str(form2.errors))
					return render(request, 'Sudakaweb/AdministradorEditarUsuario.html',ctx)
			else:
				messages.warning(request,'contraseñas !=.')
				ctx={'UsuarioForm':form,'id':id, 'UserForm':form2}
				return render(request, 'Sudakaweb/AdministradorEditarUsuario.html',ctx)

		else:
			form = UsuarioForm(instance=cliente)
			form2 = UserForm(instance= cliente.user)
			ctx={'UsuarioForm':form,'id':id, 'UserForm':form2}
			return render(request, 'Sudakaweb/AdministradorEditarUsuario.html',ctx)

class administradorEliminarCliente(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorCliente(self,request,id):
		cliente = Usuario.objects.get(pk=id)
		cliente.user.delete()
		cliente.delete()
		messages.success(request, "Se ha eliminado el usuario correctamente.")
		return HttpResponseRedirect("/AdministradorVerUsuarios")				

class administradorNuevoCliente(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorCliente(self,request):
		form = UsuarioForm(request.POST or None)
		form2 = UserForm(request.POST or None)
		if request.method=='POST':
			if request.POST['password'] == request.POST["repite_contrasena"]:
				if form.is_valid() and form2.is_valid():
					usuario = form.save()
					user = form2.save()
					user.set_password(user.password)
					user.save()
					usuario.user = user
					usuario.save()
					messages.success(request,'Se ha ingresado correctamente el nuevo cliente.')
					return HttpResponseRedirect("/AdministradorVerUsuarios")
				else:					
					if "usuarioCorreo" in form.errors:
						messages.error(request, "Debe ingresar un correo válido")
					if "usuarioTelefono" in form.errors:
						messages.error(request, "Debe ingresar un teléfono válido")
			else:
				messages.error(request,'Las contraseñas ingresadas no coinciden')
		ctx = {'UsuarioForm':form, 'UserForm':form2}
		return render(request, 'Sudakaweb/AdministradorNuevoUsuario.html',ctx)

#Menu Operario
class administradorVerOperarios(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorOperarios(self,request):
		operario = Usuario.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'operarios':operario} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerOperarios.html',ctx)

class administradorEditarOperario(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOperario(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarOperario.html',{})

class administradorNuevoOperario(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorOperario(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevoOperario.html',{})

class administradorNuevoOperario(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorOperario(self,request):
		form = UsuarioForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente el nuevo cliente.')
				return HttpResponseRedirect("/AdministradorVerClientes")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx = {'UsuarioForm':form}
		return render(request, 'Sudakaweb/AdministradorNuevoOperario.html',ctx)

#Menu PT (Puestos de trabajo)
class administradorVerPT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorPT(self,request):
		pts = PuestoDeTrabajo.objects.all()
		for pt in pts:
			pt.maquinarias = pt.maquinaria_set.all()
		ctx = {'pts':pts}
		return render(request, 'Sudakaweb/AdministradorVerPT.html',ctx)

class administradorEditarPT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorPT(self,request,id):
		pt = PuestoDeTrabajo.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = PTForm(request.POST, instance=pt)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente el puesto de trabajo.')
				return HttpResponseRedirect("/AdministradorVerPT")
			else:
				ctx={'PTForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/AdministradorEditarPT.html',ctx)
		else:
			form = PTForm(instance=pt)
			ctx={'PTForm':form,'id':id}
			return render(request, 'Sudakaweb/AdministradorEditarPT.html',ctx)

class administradorEliminarPT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorPT(self,request,id):
		pt = PuestoDeTrabajo.objects.get(pk=id)
		pt.delete()
		messages.success(request, "Se ha eliminado el puesto de trabajo correctamente.")
		return HttpResponseRedirect("/AdministradorVerPT")

class administradorNuevoPT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorPT(self,request):
		form = PTForm(request.POST or None)
		if request.method=='POST':
			messages.success(request,"editar1")
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente el nuevo puesto de trabajo.')
				return HttpResponseRedirect("/AdministradorVerPT")
			else:
				if "ptNombre" in form.errors:
					messages.error(request, "Ingrese un nombre válido")
				if "usuario" in form.errors:
					messages.error(request, "Seleccione un usuario")## por defecto
				if "materiales" in form.errors:
					messages.warning(request, request.POST)
					messages.error(request, "Error en el material")
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx = {'PTForm':form,'materiales':Material.objects.all()}
		return render(request,'Sudakaweb/AdministradorNuevoPT.html',ctx)

#Menu Maquinaria
class administradorVerMaquinarias(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorMaquinarias(self,request):
		maquinarias = Maquinaria.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'m':maquinarias} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerMaquinarias.html',ctx)

class administradorEditarMaquinaria(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorMaquinaria(self,request,id):
		maquinaria = Maquinaria.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = MaquinariaForm(request.POST, instance=maquinaria)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente la nueva Maquinaria.')
				return HttpResponseRedirect("/AdministradorVerMaquinarias")
			else:
				ctx={'MaquinariaForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/AdministradorEditarMaquinaria.html',ctx)
		else:
			form = MaquinariaForm(instance=maquinaria)
			ctx={'MaquinariaForm':form,'id':id}
			return render(request, 'Sudakaweb/AdministradorEditarMaquinaria.html',ctx)

class administradorEliminarMaquinaria(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorMaquinaria(self,request,id):
		maquinaria = Maquinaria.objects.get(pk=id)
		maquinaria.delete()
		messages.success(request, "Se ha eliminado la maquinaria.")
		return HttpResponseRedirect("/AdministradorVerMaquinarias")

class administradorNuevaMaquinaria(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevaAdministradorMaquinaria(self,request):
		form = MaquinariaForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente la nueva Maquinaria.')
				return HttpResponseRedirect("/AdministradorVerMaquinarias")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx = {'MaquinariaForm':form}
		return render(request, 'Sudakaweb/AdministradorNuevaMaquinaria.html',ctx)

#Menu SC (Solicitud de Compra)
class administradorVerSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorSC(self,request):
		sc = SolicitudDeCompra.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'scs':sc} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerSC.html',ctx)

class administradorEditarSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorSC(self,request,id):
		sc = SolicitudDeCompra.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = SCForm(request.POST, instance=sc)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente la solicitud de compra.')
				return HttpResponseRedirect("/AdministradorVerSC")
			else:
				ctx={'SCForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/AdministradorEditarSC.html',ctx)
		else:
			form = SCForm(instance=sc)
			ctx={'SCForm':form,'id':id}
			return render(request, 'Sudakaweb/AdministradorEditarSC.html',ctx)

class administradorEliminarSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorSC(self,request,id):
		sc = SolicitudDeCompra.objects.get(pk=id)
		sc.delete()
		messages.success(request, "Se ha eliminado la solicitud de compra.")
		return HttpResponseRedirect("/AdministradorVerSC")

class administradorNuevaSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevaAdministradorSC(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevaSC.html',{})


#Menu OF (Orden de Fabricación)
class administradorVerOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorOF(self,request):
		of = OrdenDeFabricacion.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'ofs':of} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerOF.html',ctx)

class administradorEditarOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOF(self,request,id):
		of = OrdenDeFabricacion.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = OFForm(request.POST, instance=of)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente la orden de fabricación.')
				return HttpResponseRedirect("/AdministradorVerOF")
			else:
				ctx={'OFForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/AdministradorEditarOF.html',ctx)
		else:
			form = OFForm(instance=of)
			ctx={'OFForm':form,'id':id}
			return render(request, 'Sudakaweb/AdministradorEditarOF.html',ctx)	

class administradorEliminarOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorOF(self,request,id):
		of = OrdenDeFabricacion.objects.get(pk=id)
		of.delete()
		messages.success(request, "Se ha eliminado la OF.")
		return HttpResponseRedirect("/AdministradorVerOF")				

class administradorNuevaOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevaAdministradorOF(self,request):
		form = OFForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente la nueva orden de fabricación.')
				return HttpResponseRedirect("/AdministradorVerOF")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx = {'OFForm':form}
		return render(request, 'Sudakaweb/AdministradorNuevaOF.html',ctx)		

#Menu OT (Orden de Trabajo)
class administradorVerOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorOT(self,request):
		ot = OrdenDeTrabajo.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'ots':ot} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerOT.html',ctx)		

class administradorEditarOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOT(self,request,id):
		ot = OrdenDeTrabajo.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = OTForm(request.POST, instance=ot)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente la orden de trabajo.')
				return HttpResponseRedirect("/AdministradorVerOT")
			else:
				ctx={'OTForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/AdministradorEditarOT.html',ctx)
		else:
			form = OTForm(instance=ot)
			ctx={'OTForm':form,'id':id}
			return render(request, 'Sudakaweb/AdministradorEditarOT.html',ctx)	

class administradorEliminarOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorOT(self,request,id):
		ot = OrdenDeTrabajo.objects.get(pk=id)
		ot.delete()
		messages.success(request, "Se ha eliminado la orden de trabajo.")
		return HttpResponseRedirect("/AdministradorVerOT")	

class administradorNuevaOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevaAdministradorOT(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevaOT.html',{})


#Menu OD (Orden de Despacho)
class administradorVerOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorOD(self,request):
		od = Despacho.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'ods':od} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerOD.html',ctx)

class administradorEditarOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOD(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarOD.html',{})

class administradorEliminarOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorOD(self,request,id):
		od = Despacho.objects.get(pk=id)
		od.delete()
		messages.success(request, "Se ha eliminado la orden de despacho.")
		return HttpResponseRedirect('/AdministradorVerOD')

#Menu OC (Orden de Compra)
class administradorVerOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorOC(self,request):
		oc = OrdenDeCompra.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'ocs':oc} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerOC.html',ctx)

class administradorEditarOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOC(self,request,id):
		oc = OrdenDeCompra.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = OFForm(request.POST, instance=oc)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente la orden de compra.')
				return HttpResponseRedirect("/AdministradorVerOC")
			else:
				ctx={'OCForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/AdministradorEditarOC.html',ctx)
		else:
			form = OFForm(instance=oc)
			ctx={'OCForm':form,'id':id}
			return render(request, 'Sudakaweb/AdministradorEditarOC.html',ctx)	

class administradorEliminarOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorOC(self,request,id):
		oc = OrdenDeCompra.objects.get(pk=id)
		oc.delete()
		messages.success(request, "Se ha eliminado la orden de compra.")
		return HttpResponseRedirect("/AdministradorVerOC")	

class administradorNuevaOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevaAdministradorOC(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevaOC.html',{})

#Menu Proveedor
class administradorVerProveedores(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorProveedores(self,request):
		proveedor = Proveedor.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'proveedores':proveedor} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/AdministradorVerProveedores.html',ctx)

class administradorEditarProveedor(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorProveedor(self,request,id):
		proveedor = Proveedor.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = ProveedorForm(request.POST, instance=proveedor)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente la nueva Proveedor.')
				return HttpResponseRedirect("/AdministradorVerProveedores")
			else:
				ctx={'ProveedorForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/AdministradorEditarProveedor.html',ctx)
		else:
			form = ProveedorForm(instance=proveedor)
			ctx={'ProveedorForm':form,'id':id}
			return render(request, 'Sudakaweb/AdministradorEditarProveedor.html',ctx)

class administradorEliminarProveedor(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarAdministradorProveedor(self,request,id):
		proveedor = Proveedor.objects.get(pk=id)
		proveedor.delete()
		messages.success(request, "Se ha eliminado el proveedor.")
		return HttpResponseRedirect("/AdministradorVerProveedores")			

class administradorNuevoProveedor(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorProveedor(self,request):
		form= ProveedorForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente el nuevo proveedor.')
				return HttpResponseRedirect("/AdministradorVerProveedores")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= {'ProveedorForm':form}
		return render(request, 'Sudakaweb/AdministradorNuevoProveedor.html',ctx)




###########################################################
#OPERARIO
###########################################################
class operarioInicio(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarOperarioInicio(self,request):
		return render(request, 'Sudakaweb/OperarioInicio.html',{})

#Menu Material
class operarioVerMateriales(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarOperarioMateriales(self,request):
		material = Material.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'materiales':material} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/OperarioVerMateriales.html',ctx)

class operarioIngresarMaterial(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def ingresarOperarioMaterial(self,request):
		return render(request, 'Sudakaweb/OperarioIngresarMaterial.html',{})

#Menu PT (Puestos de trabajo)
class operarioVerPT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarOperarioPT(self,request):
		pts = PuestoDeTrabajo.objects.all()
		for pt in pts:
			pt.maquinarias = pt.maquinaria_set.all()
		ctx = {'pts':pts}
		return render(request, 'Sudakaweb/OperarioVerPT.html',ctx)

#Menu Maquinaria
class operarioVerMaquinarias(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarOperarioMaquinarias(self,request):
		maquinarias = Maquinaria.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'m':maquinarias} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/OperarioVerMaquinarias.html',ctx)

#Menu OT (Orden de Trabajo)
class operarioVerOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarOperarioOT(self,request):
		ot = OrdenDeTrabajo.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'ots':ot} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/OperarioVerOT.html',ctx)	

class operarioEditarOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarOperarioOT(self,request):
		return render(request, 'Sudakaweb/OperarioEditarOT.html',{})

class operarioEditarOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarOperarioOT(self,request,id):
		ot = OrdenDeTrabajo.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = OTForm(request.POST, instance=ot)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente la orden de trabajo.')
				return HttpResponseRedirect("/OperarioVerOT")
			else:
				ctx={'OTForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/OperarioEditarOT.html',ctx)
		else:
			form = OTForm(instance=ot)
			ctx={'OTForm':form,'id':id}
			return render(request, 'Sudakaweb/OperarioEditarOT.html',ctx)

#Menu OD (Orden de Despacho)
class operarioVerOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarOperarioOD(self,request):
		od = Despacho.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'ods':od} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/OperarioVerOD.html',ctx)

class operarioEditarOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarOperarioOD(self,request):
		return render(request, 'Sudakaweb/OperarioEditarOD.html',{})




##########################################################
#CLIENTE
##########################################################
class clienteInicio(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarClienteInicio(self,request):
		return render(request, 'Sudakaweb/ClienteInicio.html',{})

class clienteVerSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarClienteSC(self,request):
		sc = SolicitudDeCompra.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'scs':sc} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/ClienteVerSC.html',ctx)

class clienteEditarSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarClienteSC(self,request,id):
		sc = SolicitudDeCompra.objects.get(pk=id)
		messages.success(request,"editar")
		if request.method == 'POST':
			form = SCForm(request.POST, instance=sc)
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha modificado correctamente la solicitud de compra.')
				return HttpResponseRedirect("/ClienteVerSC")
			else:
				ctx={'SCForm':form,'id':id}
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
				return render(request, 'Sudakaweb/ClienteEditarSC.html',ctx)
		else:
			form = SCForm(instance=sc)
			ctx={'SCForm':form,'id':id}
			return render(request, 'Sudakaweb/ClienteEditarSC.html',ctx)

class clienteEliminarSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarClienteSC(self,request,id):
		sc = SolicitudDeCompra.objects.get(pk=id)
		sc.delete()
		messages.success(request, "Se ha eliminado la solicitud de compra.")
		return HttpResponseRedirect("/ClienteVerSC")

class clienteNuevaSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevaClienteSC(self,request):
		return render(request, 'Sudakaweb/ClienteNuevaSC.html',{})		

#Menu OD (Orden de Despacho)
class clienteVerOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarClienteOD(self,request):
		od = Despacho.objects.all() # guardar en variable de cualquier nombre la lista de todos los objetos
		ctx = {'ods':od} # pasar a ctx la variable anterior
		return render(request, 'Sudakaweb/ClienteVerOD.html',ctx)

class clienteEditarOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarClienteOD(self,request):
		return render(request, 'Sudakaweb/ClienteEditarOD.html',{})

class clienteEliminarOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def eliminarClienteOD(self,request,id):
		od = Despacho.objects.get(pk=id)
		od.delete()
		messages.success(request, "Se ha eliminado la orden de despacho.")
		return HttpResponseRedirect('/ClienteVerOD')

