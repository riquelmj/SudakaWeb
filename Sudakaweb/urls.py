from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
	#Admin Django
    url(r'^admin/', include(admin.site.urls)),

    #generales y sesion
    url(r'^$', Home("a").mostrarHome),
    url(r'^login/', login_view, name="vista_login"),
	url(r'^logout/', logout_view, name= 'vista_logout'),

	url(r'^index$',inicio("a").mostrarInicio, name="vista_inicio"),
	url(r'^Nostros$',nosotros("a").mostrarNosotros, name="vista_nosotros"),
	url(r'^Catalogo$',catalogo("a").mostrarCatalogo, name="vista_catalogo"),
	url(r'^Contacto$',contacto("a").mostrarContacto, name="vista_contacto"),

	url(r'^RegistroCliente$',registro("a").mostrarRegistro, name="vista_registro"),


	#Vistas Administrador
	url(r'^AdministradorInicio$',administradorInicio("a").mostrarAdministradorInicio, name="vista_administrador_inicio"),
	url(r'^AdministradorVerMateriales$',administradorVerMateriales("a").mostrarAdministradorMateriales, name="vista_administrador_ver_materiales"),
	url(r'^AdministradorIngresarMaterial$',administradorIngresarMaterial("a").ingresarAdministradorMaterial, name="vista_administrador_ingresar_material"),
	url(r'^AdministradorEditarMaterial/(?P<id>([0-9]{0,50}))/$',administradorEditarMaterial("a").editarAdministradorMaterial, name="vista_administrador_editar_material"),
	url(r'^AdministradorEliminarMaterial/(?P<id>([0-9]{0,50}))/$',administradorEliminarMaterial("a").eliminarAdministradorMaterial, name="vista_administrador_eliminar_material"),
	url(r'^AdministradorNuevoMaterial$',administradorNuevoMaterial("a").nuevoAdministradorMaterial, name="vista_administrador_nuevo_material"),
	url(r'^AdministradorVerProductos$',administradorVerProductos("a").mostrarAdministradorProductos, name="vista_administrador_ver_productos"),
	url(r'^AdministradorEditarProducto$',administradorEditarProducto("a").editarAdministradorProducto, name="vista_administrador_editar_producto"),
	url(r'^AdministradorNuevoProducto$',administradorNuevoProducto("a").nuevoAdministradorProducto, name="vista_administrador_nuevo_producto"),
	url(r'^AdministradorVerUsuarios$',administradorVerClientes("a").mostrarAdministradorClientes, name="vista_administrador_ver_clientes"),
	url(r'^AdministradorEditarUsuario/(?P<id>([0-9]{0,50}))/$',administradorEditarCliente("a").editarAdministradorCliente, name="vista_administrador_editar_cliente"),
	url(r'^AdministradorEliminarUsuario/(?P<id>([0-9]{0,50}))/$',administradorEliminarCliente("a").eliminarAdministradorCliente, name="vista_administrador_eliminar_cliente"),
	url(r'^AdministradorNuevoUsuario$',administradorNuevoCliente("a").nuevoAdministradorCliente, name="vista_administrador_nuevo_cliente"),
	url(r'^AdministradorVerOperarios$',administradorVerOperarios("a").mostrarAdministradorOperarios, name="vista_administrador_ver_operarios"),
	url(r'^AdministradorEditarOperario$',administradorEditarOperario("a").editarAdministradorOperario, name="vista_administrador_editar_operario"),
	url(r'^AdministradorNuevoOperario$',administradorNuevoOperario("a").nuevoAdministradorOperario, name="vista_administrador_nuevo_operario"),
	url(r'^AdministradorVerPT$',administradorVerPT("a").mostrarAdministradorPT, name="vista_administrador_ver_pt"),
	url(r'^AdministradorEditarPT/(?P<id>([0-9]{0,50}))/$',administradorEditarPT("a").editarAdministradorPT, name="vista_administrador_editar_pt"),
	url(r'^AdministradorEliminarPT/(?P<id>([0-9]{0,50}))/$',administradorEliminarPT("a").eliminarAdministradorPT, name="vista_administrador_eliminar_pt"),
	url(r'^AdministradorNuevoPT$',administradorNuevoPT("a").nuevoAdministradorPT, name="vista_administrador_nuevo_pt"),
	url(r'^AdministradorVerMaquinarias$',administradorVerMaquinarias("a").mostrarAdministradorMaquinarias, name="vista_administrador_ver_maquinarias"),
	url(r'^AdministradorEditarMaquinaria/(?P<id>([0-9]{0,50}))/$',administradorEditarMaquinaria("a").editarAdministradorMaquinaria, name="vista_administrador_editar_maquinaria"),
	url(r'^AdministradorEliminarMaquinaria/(?P<id>([0-9]{0,50}))/$',administradorEliminarMaquinaria("a").eliminarAdministradorMaquinaria, name="vista_administrador_eliminar_maquinaria"),
	url(r'^AdministradorNuevaMaquinaria$',administradorNuevaMaquinaria("a").nuevaAdministradorMaquinaria, name="vista_administrador_nueva_maquinaria"),
	url(r'^AdministradorVerSC$',administradorVerSC("a").mostrarAdministradorSC, name="vista_administrador_ver_sc"),
	url(r'^AdministradorEditarSC/(?P<id>([0-9]{0,50}))/$',administradorEditarSC("a").editarAdministradorSC, name="vista_administrador_editar_sc"),
	url(r'^AdministradorEliminarSC/(?P<id>([0-9]{0,50}))/$',administradorEliminarSC("a").eliminarAdministradorSC, name="vista_administrador_eliminar_sc"),
	url(r'^AdministradorNuevaSC$',administradorNuevaSC("a").nuevaAdministradorSC, name="vista_administrador_nueva_sc"),
	url(r'^AdministradorVerOF$',administradorVerOF("a").mostrarAdministradorOF, name="vista_administrador_ver_of"),
	url(r'^AdministradorEditarOF/(?P<id>([0-9]{0,50}))/$',administradorEditarOF("a").editarAdministradorOF, name="vista_administrador_editar_of"),
	url(r'^AdministradorEliminarOF/(?P<id>([0-9]{0,50}))/$',administradorEliminarOF("a").eliminarAdministradorOF, name="vista_administrador_eliminar_of"),
	url(r'^AdministradorNuevaOF$',administradorNuevaOF("a").nuevaAdministradorOF, name="vista_administrador_nueva_of"),
	url(r'^AdministradorVerOT$',administradorVerOT("a").mostrarAdministradorOT, name="vista_administrador_ver_ot"),
	url(r'^AdministradorEditarOT/(?P<id>([0-9]{0,50}))/$',administradorEditarOT("a").editarAdministradorOT, name="vista_administrador_editar_ot"),
	url(r'^AdministradorEliminarOT/(?P<id>([0-9]{0,50}))/$',administradorEliminarOT("a").eliminarAdministradorOT, name="vista_administrador_eliminar_ot"),
	url(r'^AdministradorNuevaOT$',administradorNuevaOT("a").nuevaAdministradorOT, name="vista_administrador_nueva_ot"),
	url(r'^AdministradorVerOD$',administradorVerOD("a").mostrarAdministradorOD, name="vista_administrador_ver_od"),
	url(r'^AdministradorEditarOD/(?P<id>([0-9]{0,50}))/$',administradorEditarOD("a").editarAdministradorOD, name="vista_administrador_editar_od"),
	url(r'^AdministradorEliminarOD/(?P<id>([0-9]{0,50}))/$',administradorEliminarOD("a").eliminarAdministradorOD, name="vista_administrador_eliminar_od"),
	url(r'^AdministradorVerOC$',administradorVerOC("a").mostrarAdministradorOC, name="vista_administrador_ver_oc"),
	url(r'^AdministradorEditarOC/(?P<id>([0-9]{0,50}))/$',administradorEditarOC("a").editarAdministradorOC, name="vista_administrador_editar_oc"),
	url(r'^AdministradorEliminarOC/(?P<id>([0-9]{0,50}))/$',administradorEliminarOC("a").eliminarAdministradorOC, name="vista_administrador_eliminar_oc"),
	url(r'^AdministradorNuevaOC$',administradorNuevaOC("a").nuevaAdministradorOC, name="vista_administrador_nueva_oc"),
	url(r'^AdministradorVerProveedores$',administradorVerProveedores("a").mostrarAdministradorProveedores, name="vista_administrador_ver_proveedores"),
	url(r'^AdministradorEditarProveedor/(?P<id>([0-9]{0,50}))/$',administradorEditarProveedor("a").editarAdministradorProveedor, name="vista_administrador_editar_proveedor"),
	url(r'^AdministradorEliminarProveedor/(?P<id>([0-9]{0,50}))/$',administradorEliminarProveedor("a").eliminarAdministradorProveedor, name="vista_administrador_eliminar_proveedor"),
	url(r'^AdministradorNuevoProveedor$',administradorNuevoProveedor("a").nuevoAdministradorProveedor, name="vista_administrador_nuevo_proveedor"),

	#Vistas Operario
	url(r'^OperarioInicio$',operarioInicio("a").mostrarOperarioInicio, name="vista_operario_inicio"),
	url(r'^OperarioVerMateriales$',operarioVerMateriales("a").mostrarOperarioMateriales, name="vista_operario_ver_materiales"),
	url(r'^OperarioIngresarMaterial$',operarioIngresarMaterial("a").ingresarOperarioMaterial, name="vista_operario_ingresar_material"),
	url(r'^OperarioVerPT$',operarioVerPT("a").mostrarOperarioPT, name="vista_operario_ver_pt"),
	url(r'^OperarioVerMaquinarias$',operarioVerMaquinarias("a").mostrarOperarioMaquinarias, name="vista_operario_ver_maquinarias"),
	url(r'^OperarioVerOT$',operarioVerOT("a").mostrarOperarioOT, name="vista_operario_ver_ot"),
	url(r'^OperarioEditarOT/(?P<id>([0-9]{0,50}))/$',operarioEditarOT("a").editarOperarioOT, name="vista_operario_editar_ot"),
	url(r'^OperarioVerOD$',operarioVerOD("a").mostrarOperarioOD, name="vista_operario_ver_od"),
	url(r'^OperarioEditarOD/(?P<id>([0-9]{0,50}))/$',operarioEditarOD("a").editarOperarioOD, name="vista_operario_editar_od"),
	
	#Vistas Cliente
	url(r'^ClienteInicio$',clienteInicio("a").mostrarClienteInicio, name="vista_cliente_inicio"),
	url(r'^ClienteVerSC$',clienteVerSC("a").mostrarClienteSC, name="vista_cliente_ver_sc"),
	url(r'^ClienteEditarSC/(?P<id>([0-9]{0,50}))/$',clienteEditarSC("a").editarClienteSC, name="vista_cliente_editar_sc"),
	url(r'^ClienteEliminarSC/(?P<id>([0-9]{0,50}))/$',clienteEliminarSC("a").eliminarClienteSC, name="vista_cliente_eliminar_sc"),
	url(r'^ClienteNuevaSC$',clienteNuevaSC("a").nuevaClienteSC, name="vista_cliente_nueva_sc"),
	url(r'^ClienteVerOD$',clienteVerOD("a").mostrarClienteOD, name="vista_cliente_ver_od"),
	url(r'^ClienteEditarOD/(?P<id>([0-9]{0,50}))/$',clienteEditarOD("a").editarClienteOD, name="vista_cliente_editar_od"),
	url(r'^ClienteEliminarOD/(?P<id>([0-9]{0,50}))/$',clienteEliminarOD("a").eliminarClienteOD, name="vista_cliente_eliminar_od"),
	

]
