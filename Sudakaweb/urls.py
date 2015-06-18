from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
	#Admin Django
    url(r'^admin/', include(admin.site.urls)),

    #generales y sesion
    url(r'^$', Home("a").mostrarHome),
    url(r'^ordenesdecompra/listado/', oc_view, name= 'listado_oc'),
    url(r'^iniciosesion$', Login("a").mostrarLogin),
    url(r'^ModificarPerfil$', ModificarPerfil("a").mostrarModificarPerfil),
	url(r'^modificarContrasena$', ModificarContrasena("a").mostrarModificarContrasena),
	url(r'^logout/', logout_view, name= 'vista_logout'),

	#administrador
    url(r'^HomeAdmi$', HomeAdmi("a").mostrarHomeAdmi),
    url(r'^admiusuario$', AdmiUsuario("a").mostrarAdmiUsuario),
	url(r'^admiusuarioingreusuario$', AdmiUsuarioIngreUsuario("a").mostrarAdmiUsuarioIngreUsuario, name='vista_ingresar_usuario'), #Ingresar Usuario
	url(r'^admitrab$', AdmiTrab("a").mostrarAdmiTrab),
	url(r'^admitrabingretrab$', AdmiTrabIngreTrab("a").mostrarAdmiTrabIngreTrab, name='vista_ingresar_trabajador'), #Ingresar trabajador
	url(r'^admitrabmodiestado_getForm$', AdmiTrabModiEstado_getForm, name="vista_modificar_trab_get_form"),#Modificar Trabajador
	url(r'^admitrabmodiestado$', AdmiTrabModiEstado("a").mostrarAdmiTrabModiEstado,name="vista_modificar_trab"),
	url(r'^admitrabmodtrab$', AdmiTrabModTrab("a").mostrarAdmiTrabModTrab),
	url(r'^admimaqui$', AdmiMaqui("a").mostrarAdmiMaqui),
	url(r'^admimaquiverestado$', AdmiMaquiVerEstado("a").mostrarAdmiMaquiVerEstado),
	url(r'^admimaquimodiestado$', AdmiMaquiModiEstado("a").mostrarAdmiMaquiModiEstado, name='vista_modificar_estado_maquinaria'),
	url(r'^admimaquiingremaqui$', AdmiMaquiIngreMaqui("a").mostrarAdmiMaquiIngreMaqui, name='vista_ingresar_maquinaria'), ###BASE PARA INGRESAR
	url(r'^admimaquimodiestado_getForm$', AdmiMaquiModiEstado_getForm, name="vista_modificar_maqui_get_form"), ##BASE MODIFICAR ESTADO
	url(r'^adminuevaorden$', AdmiOrdenIngre("a").mostrarAdmiOrdenIngre,name="vista_ingresar_orden"),
	url(r'^getdatosoc$', boderecepcionproducto_getData,name="vista_get_datos_OC"),
	url(r'^despachar$', despachar,name="vista_despachar"),

###COSAS AGREGADA 4
	url(r'^admiadmiOC$', admiadmiOC("a").mostraradmiadmiOC),
	url(r'^admiadmiOCverestadoOC$', admiadmiOCverestadoOC("a").mostraradmiadmiOCverestadoOC),
	url(r'^admiadmiOCmodestadoOC$', admiadmiOCmodestadoOC("a").mostraradmiadmiOCmodestadoOC),
	url(r'^admiverorden$', admiVerOrden("a").mostratAdmiVerOrden),
### HASTA AQUI



	#Bodeguero
	url(r'^HomeBode$', HomeBode("a").mostrarHomeBode),
	url(r'^bodenuevomate$', BodeNuevoMate("a").mostrarBodeNuevoMate, name='vista_nuevo_material'), ###Ingresar Material nuevo
	url(r'^boderecepcionproducto$', boderecepcionproducto("a").mostrarboderecepcionproducto),
	###COSAS AGREGADAS 3
	#url(r'^bodeingremate$', bodeingremate("a").mostrarbodeingremate, name= 'mostrarbodeingremate'),
	url(r'^bodeentregamate$', bodeentregamate("a").mostrarbodeentregamate),
	url(r'^bodestock$', bodestock("a").mostrarbodestock),
	url(r'^actualizar/recibido$', actualizar_recibido,name="vista_actualizar_recibido"),



	### Hasta aqui
	
	#Vendedor
	url(r'^HomeVende$', HomeVende("a").mostrarHomeVende),
	###COSAS AGREGADAS
	url(r'^vendgenerarOT$', vendgenerarOT("a").mostrarvendgenerarOT),
	url(r'^vendconsulOC$', vendconsulOC("a").mostrarvendconsulOC),
	url(r'^vendconsulOCverestadoOC$', vendconsulOCverestadoOC("a").mostrarvendconsulOCverestadoOC),
	url(r'^vendconsulOCverestadoavanceOC$', vendconsulOCverestadoavanceOC("a").mostrarvendconsulOCverestadoavanceOC),
	url(r'^vendadmiOC$', vendadmiOC("a").mostrarvendadmiOC),
	url(r'^vendadmiOCverOC$', vendadmiOCverOC("a").mostrarvendadmiOCverOC),
	url(r'^vendadmiOCmodificarOC$', vendadmiOCmodificarOC("a").mostrarvendadmiOCmodificarOC),
	url(r'^vendeordeningre$', VendeOrdenIngre("a").mostrarVendeOrdenIngre,name="vista_ingresar_orden"),

	

	#Jefe de Taller
	url(r'^HomeJefe$', HomeJefe("a").mostrarHomeJefe),
	###COSAS AGREGADAS
	url(r'^jefetallerasigtareas$', jefetallerasigtareas("a").mostrarjefetallerasigtareas),
	url(r'^jefetallerOF$', jefetallerOF("a").mostrarjefetallerOF),
	url(r'^jefetallerOFactualavanOF$', jefetallerOFactualavanOF("a").mostrarjefetallerOFactualavanOF, name="vista_avance"),
	url(r'^jefetallerOFactualavanOF_getData$', jefetallerOFactualavanOF_getData,name="vista_get_datos_avance"),
	url(r'^jefetallerOFverestadoavanOF$', jefetallerOFverestadoavanOF("a").mostrarjefetallerOFverestadoavanOF),
	url(r'^jefetallerproductrab$', jefetallerproductrab("a").mostrarjefetallerproductrab),
	url(r'^jefetallerproductrabactualproduc$', jefetallerproductrabactualproduc("a").mostrarjefetallerproductrabactualproduc),
	url(r'^jefetallerproductrabverproduc$', jefetallerproductrabverproduc("a").mostrarjefetallerproductrabverproduc),


	url(r'^wejemplo$', wejemplo("a").wejemplo, name="wejemplo"),


	#NUEVAS VISTAS

	#Vistas Administrador
	url(r'^AdministradorInicio$',administradorInicio("a").mostrarAdministradorInicio, name="vista_administrador_inicio"),
	url(r'^AdministradorVerMateriales$',administradorVerMateriales("a").mostrarAdministradorMateriales, name="vista_administrador_ver_materiales"),
	url(r'^AdministradorIngresarMaterial$',administradorIngresarMaterial("a").ingresarAdministradorMaterial, name="vista_administrador_ingresar_material"),
	url(r'^AdministradorEditarMaterial$',administradorEditarMaterial("a").editarAdministradorMaterial, name="vista_administrador_editar_material"),
	url(r'^AdministradorNuevoMaterial$',administradorNuevoMaterial("a").nuevoAdministradorMaterial, name="vista_administrador_nuevo_material"),
	url(r'^AdministradorVerProductos$',administradorVerProductos("a").mostrarAdministradorProductos, name="vista_administrador_ver_productos"),
	url(r'^AdministradorEditarProducto$',administradorEditarProducto("a").editarAdministradorProducto, name="vista_administrador_editar_producto"),
	url(r'^AdministradorNuevoProducto$',administradorNuevoProducto("a").nuevoAdministradorProducto, name="vista_administrador_nuevo_producto"),
	url(r'^AdministradorVerClientes$',administradorVerClientes("a").mostrarAdministradorClientes, name="vista_administrador_ver_clientes"),
	url(r'^AdministradorEditarCliente$',administradorEditarCliente("a").editarAdministradorCliente, name="vista_administrador_editar_cliente"),
	url(r'^AdministradorNuevoCliente$',administradorNuevoCliente("a").nuevoAdministradorCliente, name="vista_administrador_nuevo_cliente"),
	url(r'^AdministradorVerOperarios$',administradorVerOperarios("a").mostrarAdministradorOperarios, name="vista_administrador_ver_operarios"),
	url(r'^AdministradorEditarOperario$',administradorEditarOperario("a").editarAdministradorOperario, name="vista_administrador_editar_operario"),
	url(r'^AdministradorNuevoOperario$',administradorNuevoOperario("a").nuevoAdministradorOperario, name="vista_administrador_nuevo_operario"),
	url(r'^AdministradorVerPT$',administradorVerPT("a").mostrarAdministradorPT, name="vista_administrador_ver_pt"),
	url(r'^AdministradorEditarPT$',administradorEditarPT("a").editarAdministradorPT, name="vista_administrador_editar_pt"),
	url(r'^AdministradorNuevoPT$',administradorNuevoPT("a").nuevoAdministradorPT, name="vista_administrador_nuevo_pt"),
	url(r'^AdministradorVerMaquinarias$',administradorVerMaquinarias("a").mostrarAdministradorMaquinarias, name="vista_administrador_ver_maquinarias"),
	url(r'^AdministradorEditarMaquinaria$',administradorEditarMaquinaria("a").editarAdministradorMaquinaria, name="vista_administrador_editar_maquinaria"),
	url(r'^AdministradorNuevaMaquinaria$',administradorNuevaMaquinaria("a").nuevaAdministradorMaquinaria, name="vista_administrador_nueva_maquinaria"),
	url(r'^AdministradorVerSC$',administradorVerSC("a").mostrarAdministradorSC, name="vista_administrador_ver_sc"),
	url(r'^AdministradorEditarSC$',administradorEditarSC("a").editarAdministradorSC, name="vista_administrador_editar_sc"),
	url(r'^AdministradorNuevaSC$',administradorNuevaSC("a").nuevaAdministradorSC, name="vista_administrador_nueva_sc"),
	url(r'^AdministradorVerOF$',administradorVerOF("a").mostrarAdministradorOF, name="vista_administrador_ver_of"),
	url(r'^AdministradorEditarOF$',administradorEditarOF("a").editarAdministradorOF, name="vista_administrador_editar_of"),
	url(r'^AdministradorNuevaOF$',administradorNuevaOF("a").nuevaAdministradorOF, name="vista_administrador_nueva_of"),
	url(r'^AdministradorVerOT$',administradorVerOT("a").mostrarAdministradorOT, name="vista_administrador_ver_ot"),
	url(r'^AdministradorEditarOT$',administradorEditarOT("a").editarAdministradorOT, name="vista_administrador_editar_ot"),
	url(r'^AdministradorNuevaOT$',administradorNuevaOT("a").nuevaAdministradorOT, name="vista_administrador_nueva_ot"),
	url(r'^AdministradorVerOD$',administradorVerOD("a").mostrarAdministradorOD, name="vista_administrador_ver_od"),
	url(r'^AdministradorEditarOD$',administradorEditarOD("a").editarAdministradorOD, name="vista_administrador_editar_od"),
	url(r'^AdministradorVerOC$',administradorVerOC("a").mostrarAdministradorOC, name="vista_administrador_ver_oc"),
	url(r'^AdministradorEditarOC$',administradorEditarOC("a").editarAdministradorOC, name="vista_administrador_editar_oc"),
	url(r'^AdministradorNuevaOC$',administradorNuevaOC("a").nuevaAdministradorOC, name="vista_administrador_nueva_oc"),
	url(r'^AdministradorVerProveedores$',administradorVerProveedores("a").mostrarAdministradorProveedores, name="vista_administrador_ver_proveedores"),
	url(r'^AdministradorEditarProveedor$',administradorEditarProveedor("a").editarAdministradorProveedor, name="vista_administrador_editar_proveedor"),
	url(r'^AdministradorNuevoProveedor$',administradorNuevoProveedor("a").nuevoAdministradorProveedor, name="vista_administrador_nuevo_proveedor"),

	#Vistas Operario

	#Vistas Cliente
	

]
