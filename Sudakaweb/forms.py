from django import forms
from django.forms.widgets import *
from django.forms.fields import ChoiceField
from Sudakaweb.models import *
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
	class Meta:
		model= Usuario #Tabla a referenciar
		fields= ['usuarioNombre','usuarioApellido','usuarioFechaNacimiento','usuarioTelefono','usuarioCorreo','usuarioClave','usuarioHabilitador','usuarioRol'] #atributos a ingresar
		widgets={
				'usuarioNombre': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre','style':'width:70%'}),
				'usuarioApellido': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Apellido','style':'width:70%'}),
				'usuarioFechaNacimiento': forms.DateInput(attrs={'class':'form-control col-sm-4','placeholder':'Fecha de Nacimiento','style':'width:70%'}),
				'usuarioTelefono': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Telefono','style':'width:70%'}),
				'usuarioCorreo': forms.TextInput(attrs={'class':'form-control','placeholder':'Correo','style':'width:70%'}),
				'usuarioClave': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Clave','style':'width:70%'}),
				'usuarioHabilitador': forms.TextInput(attrs={'class':'form-control','placeholder':'Habilitador','style':'width:70%'}),
				'usuarioRol': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Rol','style':'width:70%'}),
				}

class MaterialForm(forms.ModelForm):
	class Meta:
		model= Material #Tabla a referenciar
		fields= ['materialNombre','materialStock','materialStockMinimo','materialUnidadMedida','materialTipo','materialSubTipo','prodTermPrecio'] #atributos a ingresar
		widgets={
				'materialNombre': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre Material','style':'width:70%'}),
				'materialStock': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Stock Material','style':'width:70%'}),
				'materialStockMinimo': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Stock Minimo Material','style':'width:70%'}),
				'materialUnidadMedida': forms.Select(attrs={'class':'form-control','placeholder':'Unidad de medida Material','style':'width:70%'}),
				'materialTipo': forms.Select(attrs={'class':'form-control','placeholder':'Tipo Material','style':'width:70%'}),
				'materialSubTipo': forms.Select(attrs={'class':'form-control','placeholder':'Subtipo Material','style':'width:70%'}),
				'prodTermPrecio': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Precio Material','style':'width:70%'}),
				}

class PTForm(forms.ModelForm):
	class Meta:
		model= PuestoDeTrabajo #Tabla a referenciar
		fields= ['ptNombre','usuario','materiales'] #atributos a ingresar
		widgets={
				'ptNombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre PT','style':'width:70%'}),
				'usuario': forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario','style':'width:70%'}),
				'materiales': forms.TextInput(attrs={'class':'form-control','placeholder':'materiales','style':'width:70%'})
				}

class MaquinariaForm(forms.ModelForm):
	class Meta:
		model= Maquinaria #Tabla a referenciar
		fields= ['maqNombre','maqEstado','pt'] #atributos a ingresar
		widgets={
				'maqNombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','style':'width:70%'}),
				'maqEstado': forms.Select(attrs={'class':'form-control','placeholder':'Nombre Proveedor','style':'width:70%'}),
				'pt': forms.Select(attrs={'class':'form-control','placeholder':'Direccion Proveedor','style':'width:70%'}),
				}

class SCForm(forms.ModelForm):
	class Meta:
		model= SolicitudDeCompra #Tabla a referenciar
		fields= ['solicitudFecha','usuario','estadoSolicitud'] #atributos a ingresar
		widgets={
				'solicitudFecha': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha','style':'width:70%'}),
				'usuario': forms.Select(attrs={'class':'form-control','placeholder':'Nombre Proveedor','style':'width:70%'}),
				'estadoSolicitud': forms.Select(attrs={'class':'form-control','placeholder':'Nombre Proveedor','style':'width:70%'})
				}

class OFForm(forms.ModelForm):
	class Meta:
		model= OrdenDeFabricacion #Tabla a referenciar
		fields= ['ofCant','ofFechaIngreso','ofFechaInicio','ofFechaTermino','material','usuario','estadoOF'] #atributos a ingresar
		widgets={
				'ofCant': forms.TextInput(attrs={'class':'form-control','placeholder':'Cantidad','style':'width:70%'}),
				'ofFechaIngreso': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Ingreso OF','style':'width:70%'}),
				'ofFechaInicio': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Inicio','style':'width:70%'}),
				'ofFechaTermino': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Termino','style':'width:70%'}),
				'material': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Termino','style':'width:70%'}),
				'usuario': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Termino','style':'width:70%'}),
				'estadoOF': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Termino','style':'width:70%'})
				}

class OCForm(forms.ModelForm):
	class Meta:
		model= OrdenDeCompra #Tabla a referenciar
		fields= ['ordenCompraFechaEmision','proveedor'] #atributos a ingresar
		widgets={
				'ordenCompraFechaEmision': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha','style':'width:70%'}),
				'proveedor': forms.Select(attrs={'class':'form-control','placeholder':'Nombre Proveedor','style':'width:70%'})
				}

class ODForm(forms.ModelForm):
	class Meta:
		model= Despacho #Tabla a referenciar
		fields= ['despachoDireccion','despachoFecha','solicitud','comuna'] #atributos a ingresar
		widgets={
				'despachoDireccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion','style':'width:70%'}),
				'despachoFecha': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha de despacho','style':'width:70%'}),
				'solicitud': forms.TextInput(attrs={'class':'form-control','placeholder':'N Solicitud de compra','style':'width:70%'}),
				'comuna': forms.TextInput(attrs={'class':'form-control','placeholder':'Comuna','style':'width:70%'})
				}

class ProveedorForm(forms.ModelForm):
	class Meta:
		model= Proveedor #Tabla a referenciar
		fields= ['proveedorRut','proveedorNombre','proveedorDireccion','proveedorTelefono','proveedorCorreo'] #atributos a ingresar
		widgets={
				'proveedorRut': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Rut Proveedor','style':'width:70%'}),
				'proveedorNombre': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre Proveedor','style':'width:70%'}),
				'proveedorDireccion': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Direccion Proveedor','style':'width:70%'}),
				'proveedorTelefono': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Telefono Proveedor','style':'width:70%'}),
				'proveedorCorreo': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Correo Proveedor','style':'width:70%'})
				}
	

'''
####Ingresar Usuario
class UsuarioForm(forms.ModelForm):
	class Meta:
		model= Usuario #Tabla a referenciar
		exclude= ("user",)
		fields= ['rutUsuario','nombreUsuario','apellidoUsuario'] #atributos a ingresar
		widgets={
				'rutUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Rut','style':'width:50%'}),
				'nombreUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre','style':'width:50%'}),
				'apellidoUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Apellido','style':'width:50%'}),
			}
class RolForm(forms.ModelForm):
	class Meta:
		model= Rol #Tabla a referenciar
		fields= ['rol'] #atributos a ingresar
		widgets={
				'rol': forms.Select(attrs={'class':'form-control','placeholder':'Rol','style':'width:50%'}),
				
			}


###BASE PARA LOS INGRESAR
class MaquinariaForm(forms.ModelForm):
	class Meta:
		model= PuestoTrabajo
		fields= ['puestoTrabajo','estadoMaquinaria']
		widgets={
			'puestoTrabajo': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre','style':'width:50%'}),
			'estadoMaquinaria': forms.Select(attrs={'class':'form-control','placeholder':'Nombre','style':'width:50%'})
		}


####Ingresar Trabajador
class OperadorForm(forms.ModelForm):
	class Meta:
		model= Operador #Tabla a referenciar
		fields= ['rutOperador','nombreOperador','apellidoOperador','mailOperador','estadoOperador'] #atribitos a ingresar
		widgets={
				'rutOperador': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Rut','style':'width:50%'}),
				'nombreOperador': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre','style':'width:50%'}),
				'apellidoOperador': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Apellido','style':'width:50%'}),
				'mailOperador': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Mail','style':'width:50%'}),
				'estadoOperador': forms.Select(attrs={'class':'form-control','placeholder':'Estado','style':'width:50%'})
			}

####Ingresar material nuevo 
class MaterialForm(forms.ModelForm):
	class Meta:
		model= Material #Tabla a referenciar
		fields= ['nombreMaterial','cantidad','unidadMedida','tipoMaterial'] #atributos a ingresar
		widgets={
				'nombreMaterial': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre Material','style':'width:50%'}),
				'cantidad': forms.TextInput(attrs={'type':'number','class':'form-control col-sm-4','placeholder':'Cantidad','style':'width:50%'}),
				'unidadMedida': forms.Select(attrs={'class':'form-control','placeholder':'Unidad de Medida','style':'width:50%'}),
				'tipoMaterial': forms.Select(attrs={'class':'form-control','placeholder':'Tipo de Material','style':'width:50%'})
			}

#################################INTENTO AGREGAR USUARIOS

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder': 'Username','style':'width:50%'}),  
            'password': forms.PasswordInput(attrs={'class':'form-control col-sm-4','placeholder': 'Password','style':'width:50%'}),
        }

class TipoProductoForm(forms.ModelForm):
	class Meta:
		model= TipoProducto #Tabla a referenciar
		fields= ['nombreTP',] #atributos a ingresar
		widgets={
				'nombreTP': forms.Select(attrs={'class':'form-control','placeholder':'Tipo de Producto','style':'width:50%'})
			}

class OrdenCompraForm(forms.ModelForm):
	class Meta:
		model= OrdenDeCompra #Tabla a referenciar
		fields= ['numeroOC'] #atributos a ingresar
		widgets={
				'numeroOC': forms.Select(attrs={'class':'form-control','placeholder':'Numero OC','style':'width:50%'}),
				
			}'''