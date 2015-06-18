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
from datetime import *

# Create your views here.
class Home(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHome(self,request):
		context= {'pelicula':''}
		return render(request, 'Sudakaweb/home.html',context)

class HomeAdmi(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHomeAdmi(self,request):
		return render(request, 'Sudakaweb/homeAdmi.html',{})

class HomeBode(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHomeBode(self,request):
		return render(request, 'Sudakaweb/homeBode.html',{})

class HomeVende(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHomeVende(self,request):
		return render(request, 'Sudakaweb/homeVende.html',{})

class HomeJefe(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHomeJefe(self,request):
		return render(request, 'Sudakaweb/homeJefe.html',{})

class ModificarPerfil(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarModificarPerfil(self,request):
		return render(request, 'Sudakaweb/modificarPerfil.html',{})

class ModificarContrasena(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarModificarContrasena(self,request):
		return render(request, 'Sudakaweb/modificarContrasena.html',{})

class AdmiUsuario(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiUsuario(self,request):
		return render(request, 'Sudakaweb/admiusuario.html',{})

class AdmiTrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrab(self,request):
		return render(request, 'Sudakaweb/admitrab.html',{})

class AdmiTrabIngreTrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrabIngreTrab(self,request):
		return render(request, 'Sudakaweb/admitrabingretrab.html',{})

class AdmiTrabModTrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrabModTrab(self,request):

		return render(request, 'Sudakaweb/admitrabmodtrab.html',{})

class AdmiMaqui(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaqui(self,request):
		return render(request, 'Sudakaweb/admimaqui.html',{})

class AdmiMaquiVerEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiVerEstado(self,request):
		return render(request, 'Sudakaweb/admimaquiverestado.html',{})

class AdmiMaquiModiEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiModiEstado(self,request):
		return render(request, 'Sudakaweb/admimaquimodiestado.html',{})

#Lista todas las ordenes de compra de sistema
def oc_view(request):
	ordenes= OrdenDeCompra.objects.all()
	ctx ={'oc':ordenes}
	return render_to_response('Sudakaweb/oc.html',ctx,context_instance=RequestContext(request))


####BASE PARA INGRESAR
class AdmiMaquiIngreMaqui(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiIngreMaqui(self,request):
		form= MaquinariaForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				duplicidad = PuestoTrabajo.objects.filter(puestoTrabajo=request.POST["puestoTrabajo"])
				if len(duplicidad)==0:
					form.save()
					messages.success(request,'Se ha ingresado correctamente la maquinaria.')
					return HttpResponseRedirect("/admimaqui")
				else:
					messages.error(request, "Ya existe una maquinaria registrada con ese nombre.")
			else:
				messages.error(request,'Debe llenar todos los campos disponibles.')
		ctx= {'MaquinariaForm':form}
		return render(request, 'Sudakaweb/admimaquiingremaqui.html',ctx)

####Ingresar Usuario
class AdmiUsuarioIngreUsuario(TemplateView):
	def __init__(self,valor):
		self.valor = valor

	def mostrarAdmiUsuarioIngreUsuario(self,request):
		form= UsuarioForm()
		form2= UserForm()
		form3= RolForm()
		
		roles = {} 
		if "check-admi" in request.POST: 
			roles["admin"] = True 
		if "check-vende" in request.POST: 
			roles["vende"] = True 
		if "check-jefe" in request.POST: 
			roles["jefe"] = True 
		if "check-bode" in request.POST: 
			roles["bode"] = True
		form= UsuarioForm(request.POST or None)
		form2= UserForm(request.POST or None)
		if request.method=='POST':
			if form2.is_valid() and form.is_valid():
					password = form2.cleaned_data['password']
					username = form2.cleaned_data['username']
					user = User()
					user.username = username
					user.set_password(password)
					user.save()
					usuario= form.save(commit=False)
					usuario.user= user
					usuario.save()
					if "check-admi" in request.POST: 
						r = Rol(rol="Administrador", usuario= usuario) 
						r.save() 
					if "check-vende" in request.POST: 
						r = Rol(rol="Vendedor", usuario= usuario) 
						r.save()
					if "check-jefe" in request.POST: 
						r = Rol(rol="Jefe de Taller", usuario= usuario) 
						r.save() 
					if "check-bode" in request.POST: 
						r = Rol(rol="Bodeguero", usuario= usuario) 
						r.save()
											
					messages.success(request,'Se ha ingresado correctamente el usuario.')
					return HttpResponseRedirect("/admiusuario")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= { 'UsuarioForm':form,'UserForm':form2, 'roles':roles}
		return render(request, 'Sudakaweb/admiusuarioingreusuario.html',ctx)



####Ingresar Operador
class AdmiTrabIngreTrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrabIngreTrab(self,request):
		form= OperadorForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente el trabajador.')
				return HttpResponseRedirect("/admitrab")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= {'OperadorForm':form}
		return render(request, 'Sudakaweb/admitrabingretrab.html',ctx)



#######Modificar Estado Trabajador
class AdmiTrabModiEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrabModiEstado(self,request):
		traba = Operador.objects.all().order_by('nombreOperador')
		form = OperadorForm(request.POST or None)
		if request.method=='POST':
			if "rutOperador" in request.POST:
				trab = Operador.objects.filter(pk=request.POST["rutOperador"])[0]
				trab.estadoOperador = request.POST["estadoOperador"]
				trab.mailOperador = request.POST["mailOperador"]
				trab.nombreOperador = request.POST["nombreOperador"]
				trab.apellidoOperador = request.POST["apellidoOperador"]
				trab.save()
				messages.success(request,'Se ha modificado correctamente el estado del trabajador.')
				return HttpResponseRedirect("/admitrab")
			else:
				messages.error(request,'Valor incorrecto para el estado del trabajador.')
		ctx = {'trabajadores':traba,'OperadorForm':form}
		return render(request, 'Sudakaweb/admitrabmodiestado.html',ctx)

@csrf_exempt
def AdmiTrabModiEstado_getForm(request):
	if "id" in request.POST and request.POST["id"]!="":
		trab = Operador.objects.get(pk=request.POST["id"])
		form = OperadorForm(instance=trab)
		ctx={
			'OperadorForm':form,
			'idOperador':request.POST["id"]
		}
		return render(request, 'Sudakaweb/admitrabmodiestado_getForm.html',ctx)
	else:
		return HttpResponse("")


####Ingresar nuevo material
class BodeNuevoMate(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarBodeNuevoMate(self,request):
		form= MaterialForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente el material.')
				return HttpResponseRedirect("/HomeBode")
				
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= {'MaterialForm':form}
		return render(request, 'Sudakaweb/bodenuevomate.html',ctx)


#######3Modificar Estado Maquina
class AdmiMaquiModiEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiModiEstado(self,request):
		maquis = PuestoTrabajo.objects.all().order_by('puestoTrabajo')
		form = MaquinariaForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				maqui = PuestoTrabajo.objects.filter(puestoTrabajo=request.POST["puestoTrabajo"])[0]
				maqui.estadoMaquinaria = request.POST["estadoMaquinaria"]
				maqui.save()
				messages.success(request,'Se ha modificado correctamente el estado de la maquinaria.')
				return HttpResponseRedirect("/admimaqui")
			else:
				messages.error(request,'Valor incorrecto para el estado de la maquinaria')
		ctx = {'maquinarias':maquis,'MaquinariaForm':form}
		return render(request, 'Sudakaweb/admimaquimodiestado.html',ctx)

@csrf_exempt
def AdmiMaquiModiEstado_getForm(request):
	maqui = PuestoTrabajo.objects.get(pk=request.POST["id"])
	form = MaquinariaForm(instance=maqui)
	ctx={
		'MaquinariaForm':form,
	}
	return render(request, 'Sudakaweb/admimaquimodiestado_getForm.html',ctx)


###Ver Estado
class AdmiMaquiVerEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiVerEstado(self,request):
		maquinarias = PuestoTrabajo.objects.all().order_by("puestoTrabajo")
		ctx = {"maquinarias":maquinarias}
		return render(request, 'Sudakaweb/admimaquiverestado.html',ctx)
		

class Login(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarLogin(self,request):
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
					usuario= Usuario.objects.filter(user=user)
					roles = Rol.objects.filter(usuario=usuario).filter(rol=request.POST['rol'])
					#if len(usuario)==1:
					if len(usuario)==1 and len(roles)>0:
						request.session['ROL_USUARIO']= request.POST['rol']
						login(request, user)
						messages.success(request,'Bienvenido ' + usuario[0].usuarioNombre)
						return HttpResponseRedirect('/')
			messages.error(request,'Usuario o Contrasena incorrectos')
			return render(request, 'Sudakaweb/login.html',{})

def logout_view(request):
    """
    Cierra la sesion de un usuario y lo redirecciona al home
    """
    logout(request)
    return HttpResponseRedirect('/')


class AdmiOrdenIngre(TemplateView):
	def __init__(self,valor):
		self.valor=valor
	def mostrarAdmiOrdenIngre(self, request):
		ctx = {}
		return render_to_response("Sudakaweb/admiordeningre.html", ctx, context_instance=RequestContext(request))


###COSAS AGREGADAS
class vendgenerarOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendgenerarOT(self,request):
		oc = OrdenDeCompra.objects.all()
		if request.method=='POST':
			orden= request.POST.get('generar')
			ordenDeCompra= OrdenDeCompra.objects.get(id=orden)
			ordenDeTrabajo= OrdenTrabajo()
			ordenDeTrabajo.ordenDeCompra= ordenDeCompra
			user=User.objects.get(username=request.user.username)
			ordenDeTrabajo.usuario= user.usuario
			ordenDeTrabajo.save()
			est = Estado.objects.get(nombreEstado="Aprobada")
			ordenDeCompra.estado = est
			ordenDeCompra.save()
			messages.success(request, "Se ha aceptado correctamente la orden de compra.")
		ctx = {'ordenes':oc}
		return render(request, 'Sudakaweb/vendgenerarOT.html', ctx)

class VendeOrdenIngre(TemplateView):
	def __init__(self,valor):
		self.valor=valor
	def mostrarVendeOrdenIngre(self, request):
		numeroOrden = OrdenDeCompra.objects.all()
		if len(numeroOrden)>0:
			numeroOrden = OrdenDeCompra.objects.all().order_by("-numeroOC")[:1][0].numeroOC+1
		else:
			numeroOrden = 1
		productos   = TipoProducto.objects.all()
		terminacion = Terminacion.objects.all()
		vendedores  = Rol.objects.filter(rol="Vendedor")
		data={}
		if request.method == "POST":
			data["nombreEmpresa"]=request.POST["nombreEmpresa"]
			data["rutEmpresa"]=request.POST["rutEmpresa"]
			data["fechaIngreso"]=request.POST["fechaIngreso"]
			data["fechaEntrega"]=request.POST["fechaEntrega"]
			flag = True
			if request.POST["nombreEmpresa"]=="":
				messages.warning(request, "Nombre de empresa vacio.")
				flag = False
			if request.POST["rutEmpresa"]=="":
				messages.warning(request, "Rut de empresa vacio.")
				flag = False
			if request.POST["fechaIngreso"]=="":
				messages.warning(request, "Ingrese fecha ingreso.")
				flag = False
			if request.POST["fechaEntrega"]=="":
				messages.warning(request, "Ingrese fecha entrega.")
				flag = False
			if flag:
				#guardar
				vendedor = Usuario.objects.filter(user = request.user)[0]
				estado = Estado.objects.get(nombreEstado="Pendiente")
				oc = OrdenDeCompra(numeroOC=1, fechaIngreso=data["fechaIngreso"],fechaEntrega=data["fechaEntrega"] , nombreEmpresa=data["nombreEmpresa"], rutEmpresa= data["rutEmpresa"],usuario=vendedor,estado=estado, )
				oc.save()
				oc.numeroOC = oc.id+1020
				oc.save()
				data = request.POST["descripcionOC"][:-1].split("&")
				messages.info(request, data)
				if data[0]!="":
					for det in data:
						valores = det.split("~")
						tipoProd = TipoProducto.objects.filter(pk=int(valores[0]))[0]
						term = Terminacion.objects.filter(pk=int(valores[2]))[0]
						p = Producto(cantidad=valores[3],cantidadRecepcionada=0,cantidadProducida=0,descripcion=valores[1],ordenDeCompra=oc, tipoProducto=tipoProd)
						p.save()
						tp = TerminacionProducto(terminacion=term, producto=p)
						tp.save()
				messages.success(request, "Orden de compra registrada con exito")
				return HttpResponseRedirect("/vendeordeningre")
		ctx = {'vendedores':vendedores, 'terminacion':terminacion, 'productos':productos, 'data':data, 'numeroOrden':numeroOrden}
		return render_to_response("Sudakaweb/vendeordeningre.html", ctx, context_instance=RequestContext(request))

class vendconsulOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendconsulOC(self,request):
		return render(request, 'Sudakaweb/vendconsulOC.html',{})

class vendconsulOCverestadoOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendconsulOCverestadoOC(self,request):
		return render(request, 'Sudakaweb/vendconsulOCverestadoOC.html',{})

class vendconsulOCverestadoavanceOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendconsulOCverestadoavanceOC(self,request):
		return render(request, 'Sudakaweb/vendconsulOCverestadoavanceOC.html',{})

class vendadmiOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendadmiOC(self,request):
		return render(request, 'Sudakaweb/vendadmiOC.html',{})

class vendadmiOCmodificarOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendadmiOCmodificarOC(self,request):
		return render(request, 'Sudakaweb/vendadmiOCmodificarOC.html',{})

class vendadmiOCverOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendadmiOCverOC(self,request):
		return render(request, 'Sudakaweb/vendadmiOCverOC.html',{})

# COSAS AGREGADAS 2

class jefetallerasigtareas(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerasigtareas(self,request):
		return render(request, 'Sudakaweb/jefetallerasigtareas.html',{})

class jefetallerOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerOF(self,request):
		return render(request, 'Sudakaweb/jefetallerOF.html',{})



class jefetallerOFactualavanOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerOFactualavanOF(self,request):
		otes=OrdenTrabajo.objects.exclude(ordenDeCompra__estado__nombreEstado="Pendiente").exclude(ordenDeCompra__estado__nombreEstado="Despachada")
		ctx = {'otes': otes}
		if request.method == "POST":
			flag = False
			for campo in request.POST:
				if campo[:4]=="ide-":
					ide = campo[4:]
					prod = Producto.objects.get(pk=ide)
					if prod.cantidad >= prod.cantidadProducida+int(request.POST["cantidad-nueva"]):
						prod.cantidadProducida = prod.cantidadProducida+int(request.POST["cantidad-nueva"]) 
						estado = Estado.objects.get(nombreEstado="En fabricación")
						aux = prod.ordenDeCompra
						aux.estado = estado
						aux.save()
						prod.save()
						flag = True
					else:
						messages.warning(request, "La caantidad ingresada exede el máximo necesario para "+str(prod.tipoProducto))
			if flag:
				messages.success(request, "Actualizado con éxito")
			ctx["selected"] = request.POST["id-ot"]


		return render(request, 'Sudakaweb/jefetallerOFactualavanOF.html',ctx)

@csrf_exempt
def jefetallerOFactualavanOF_getData(request):
	orden = OrdenTrabajo.objects.get(pk=request.POST["id-ot"])
	prods = TerminacionProducto.objects.filter(producto__ordenDeCompra=orden.ordenDeCompra)
	ctx={
		'ot':orden,
		'productos':prods
	}
	return render(request, 'Sudakaweb/jefetallerOFactualavanOF_getData.html',ctx)




class jefetallerOFverestadoavanOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerOFverestadoavanOF(self,request):
		return render(request, 'Sudakaweb/jefetallerOFverestadoavanOF.html',{})

class jefetallerproductrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerproductrab(self,request):
		return render(request, 'Sudakaweb/jefetallerproductrab.html',{})

class jefetallerproductrabactualproduc(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerproductrabactualproduc(self,request):
		return render(request, 'Sudakaweb/jefetallerproductrabactualproduc.html',{})

class jefetallerproductrabverproduc(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerproductrabverproduc(self,request):
		return render(request, 'Sudakaweb/jefetallerproductrabverproduc.html',{})


#######Bodeguero
class boderecepcionproducto(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarboderecepcionproducto(self,request):
		ordenes = OrdenTrabajo.objects.exclude(ordenDeCompra__estado__nombreEstado="Despachada").exclude(ordenDeCompra__estado__nombreEstado="Pendiente")
		ctx = {'ordenes':ordenes}
		return render(request, 'Sudakaweb/boderecepcionproducto.html',ctx)


class admiVerOrden(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostratAdmiVerOrden(self,request):
		ordenes = OrdenDeCompra.objects.all()
		ctx = {'ordenes':ordenes}
		return render(request, 'Sudakaweb/admiverorden.html',ctx)

@csrf_exempt
def actualizar_recibido(request):
	if "cantidad-nueva" in request.POST:
		ret = 0
		for key in request.POST:
			if key[:4] == "ide-":
				if ret == 0:
					ret = 1
				prod = Producto.objects.get(pk=request.POST[key])
				prod.cantidadRecepcionada = prod.cantidadRecepcionada+ int(request.POST["cantidad-nueva"])
				if prod.cantidadRecepcionada <= prod.cantidad:
					prod.save()
				else:
					ret = 2
	return HttpResponse(ret)

@csrf_exempt
def boderecepcionproducto_getData(request):
	orden = OrdenDeCompra.objects.get(pk=request.POST["id"])
	#productos = Producto.objects.filter(ordenDeCompra=orden)
	prods = TerminacionProducto.objects.filter(producto__ordenDeCompra=orden)
	ctx={
		'oc':orden,
		'productos':prods
	}
	if "generaOT" in request.POST:
		ctx["generaOT"]=1
	if "boton" in request.POST:
		ctx["verBoton"]=1
		ctx["despachar"]=1

		for prod in prods:
			if prod.producto.cantidad > prod.producto.cantidadRecepcionada:
				ctx["despachar"]=0
	return render(request, 'Sudakaweb/boderecepcionproducto_getData.html',ctx)

@csrf_exempt
def despachar(request):
	orden = OrdenDeCompra.objects.get(pk=request.POST["id"])
	usuario = Usuario.objects.filter(user= User.objects.get(username=request.user.username))[0]
	orden.estado = Estado.objects.get(nombreEstado = "Despachada")
	orden.save()
	des = Despacho(fechaDespacho=datetime.now(), ordenDeCompra=orden,usuario=usuario)
	des.save()
	ctx={
		'oc':orden
	}
	messages.success(request,"Despacho registrado correctamente.")
	return HttpResponse("")

#################################INTENTO AGREGAR USUARIOS
def registro_view(request):

	form_user = UserForm(request.POST or None) #Agregada
	#form_usuario = UsuarioForm(request.POST or None) #Agregada

	if request.POST:
		if form_user.is_valid() and form_usuario.is_valid():
			
			clave = form_user.cleaned_data['nombre'] #password y ClaveRepetida son los NAMES que tienen los inputs en el html
			clave2 = form_user.cleaned_data['nombre']
			if clave == clave2:
				if form_user.cleaned_data['username'] == '' or form_user.cleaned_data['username'] == None or clave == '' == '': # verifica que todos los campos obligatorios esten llenados
					messages.warning(request, "El nombre de usuario y clave no pueden ser nulos")
					HttpResponseRedirect("/admiusuario")
				else:
					usuarioo = User.objects.create_user(form_user.cleaned_data['username'],clave)
					usuarioo.save() #aqui se ingreso el usuario a la tabla de Django (auth_user)
			else:
				messages.warning(request,"Las claves ingresadas no coinciden")
				return HttpResponseRedirect("/admiusuario")		
		
			if form_socio.is_valid() and form_user.is_valid():
				usuario_inst = User.objects.get(username = form_user.cleaned_data['username']) #obtiene el user que ya se agrego, porke es necesario para crear el Usuario	
				if form_user.cleaned_data['nombre'] != "":
					#en la linea siguiente se crea el socio, los campos user, nacionalidad, nombre, etc son los atributos de Socio en el models, los valores entre comillas son los names que debiesen ser los mismos nombres si es ke se esta usando un modelForm
					usuario = Usuario(user=usuarioo_inst,username=form_user.cleaned_data['Username'],password=form_socio.cleaned_data['nombre'])
					usuario.save() #se crea el socio y se guarda
					messages.success(request,"El registro se ha realizado exitosamente")
					return HttpResponseRedirect('/')
				else:
					messages.warning(request,"El nombre de usuario no puede ser vacio")
					return HttpResponseRedirect('/registro')	
		messages.warning(request,"Error en los datos ingresados")
		return HttpResponseRedirect('/registro')							
	
	ctx = {'form_user': form_user,'form_usuario':form_socio}
	return render_to_response('Sudakaweb/admiordeningre.html', ctx, context_instance=RequestContext(request))


	###COSAS AGREGADAS 3

'''class bodeingremate(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarbodeingremate(self,request):
######################3


		form= MaterialForm(request.POST or None)
					if request.method=='POST':
						if form.is_valid():
							##################
							materialTemp = 
							aux = material.objects.get(tipo='materialTemp')
							aux.cantidad = aux.cantidad + nuevocantidad
							aux.save()
							###################
							form.save()
							messages.success(request,'Se ha ingresado correctamente el material.')
							return HttpResponseRedirect("/HomeBode")
							
						else:
							messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
					ctx= {'MaterialForm':form}
		########################################3
		return render(request, 'Sudakaweb/bodeingremate.html',{})
'''



class bodeentregamate(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarbodeentregamate(self,request):
		return render(request, 'Sudakaweb/bodeentregamate.html',{})

class bodestock(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarbodestock(self,request):
		return render(request, 'Sudakaweb/bodestock.html',{})

###COSAS AGREGADAS 4

class admiadmiOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostraradmiadmiOC(self,request):
		return render(request, 'Sudakaweb/admiadmiOC.html',{})

class admiadmiOCverestadoOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostraradmiadmiOCverestadoOC(self,request):
		return render(request, 'Sudakaweb/admiadmiOCverestadoOC.html',{})

class admiadmiOCmodestadoOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostraradmiadmiOCmodestadoOC(self,request):
		return render(request, 'Sudakaweb/admiadmiOCmodestadoOC.html',{})

class wejemplo(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def wejemplo(self,request):
		return render(request, 'Sudakaweb/wejemplo.html',{})

### NUEVAS CLASES

class administradorInicio(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorInicio(self,request):
		return render(request, 'Sudakaweb/AdministradorInicio.html',{})

#Menu Material
class administradorVerMateriales(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorMateriales(self,request):
		return render(request, 'Sudakaweb/AdministradorVerMateriales.html',{})

class administradorIngresarMaterial(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def ingresarAdministradorMaterial(self,request):
		return render(request, 'Sudakaweb/AdministradorIngresarMaterial.html',{})

class administradorEditarMaterial(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorMaterial(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarMaterial.html',{})

class administradorNuevoMaterial(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorMaterial(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevoMaterial.html',{})

#Menu Producto
class administradorVerProductos(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorProductos(self,request):
		return render(request, 'Sudakaweb/AdministradorVerProductos.html',{})

class administradorEditarProducto(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorProducto(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarProducto.html',{})

class administradorNuevoProducto(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorProducto(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevoProducto.html',{})

#Menu Cliente
class administradorVerClientes(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorClientes(self,request):
		return render(request, 'Sudakaweb/AdministradorVerClientes.html',{})

class administradorEditarCliente(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorCliente(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarCliente.html',{})

class administradorNuevoCliente(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorCliente(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevoCliente.html',{})

#Menu Operario
class administradorVerOperarios(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorOperarios(self,request):
		return render(request, 'Sudakaweb/AdministradorVerOperarios.html',{})

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

#Menu PT (Puestos de trabajo)
class administradorVerPT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorPT(self,request):
		return render(request, 'Sudakaweb/AdministradorVerPT.html',{})

class administradorEditarPT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorPT(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarPT.html',{})

class administradorNuevoPT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorPT(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevoPT.html',{})

#Menu Maquinaria
class administradorVerMaquinarias(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorMaquinarias(self,request):
		return render(request, 'Sudakaweb/AdministradorVerMaquinarias.html',{})

class administradorEditarMaquinaria(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorMaquinaria(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarMaquinaria.html',{})

class administradorNuevaMaquinaria(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevaAdministradorMaquinaria(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevaMaquinaria.html',{})


#Menu SC (Solicitud de Compra)
class administradorVerSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorSC(self,request):
		return render(request, 'Sudakaweb/AdministradorVerSC.html',{})

class administradorEditarSC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorSC(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarSC.html',{})

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
		return render(request, 'Sudakaweb/AdministradorVerOF.html',{})

class administradorEditarOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOF(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarOF.html',{})

class administradorNuevaOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevaAdministradorOF(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevaOF.html',{})

#Menu OT (Orden de Trabajo)
class administradorVerOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorOT(self,request):
		return render(request, 'Sudakaweb/AdministradorVerOT.html',{})

class administradorEditarOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOT(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarOT.html',{})

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
		return render(request, 'Sudakaweb/AdministradorVerOD.html',{})

class administradorEditarOD(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOD(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarOD.html',{})

#Menu OC (Orden de Compra)
class administradorVerOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdministradorOC(self,request):
		return render(request, 'Sudakaweb/AdministradorVerOC.html',{})

class administradorEditarOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorOC(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarOC.html',{})

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
		return render(request, 'Sudakaweb/AdministradorVerProveedores.html',{})

class administradorEditarProveedor(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def editarAdministradorProveedor(self,request):
		return render(request, 'Sudakaweb/AdministradorEditarProveedor.html',{})

class administradorNuevoProveedor(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def nuevoAdministradorProveedor(self,request):
		return render(request, 'Sudakaweb/AdministradorNuevoProveedor.html',{})

