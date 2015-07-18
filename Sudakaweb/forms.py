from django import forms
from django.forms.widgets import *
from django.forms.fields import ChoiceField
from Sudakaweb.models import *
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
	class Meta:
		model= Usuario #Tabla a referenciar
		fields= ['usuarioNombre','usuarioApellido','usuarioFechaNacimiento','usuarioTelefono','usuarioCorreo','usuarioHabilitador','usuarioRol'] #atributos a ingresar
		exclude= ("user",)
		widgets={
				'usuarioNombre': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Nombre','style':'width:70%'}),
				'usuarioApellido': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Apellido','style':'width:70%'}),
				'usuarioFechaNacimiento': forms.DateInput(attrs={'required':'required','class':'form-control col-sm-4','type':'date','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'usuarioTelefono': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Telefono','style':'width:70%'}),
				'usuarioCorreo': forms.TextInput(attrs={'required':'required','class':'form-control', 'type':'email','placeholder':'Correo','style':'width:70%'}),
				'usuarioHabilitador': forms.Select(attrs={'required':'required','class':'form-control','placeholder':'Habilitador','style':'width:70%'}),
				'usuarioRol': forms.Select(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Rol','style':'width:70%'}),
				}

class ClienteForm(forms.ModelForm):
	class Meta:
		model= Usuario #Tabla a referenciar
		fields= ['usuarioNombre','usuarioApellido','usuarioFechaNacimiento','usuarioTelefono','usuarioCorreo'] #atributos a ingresar
		exclude= ("user",)
		widgets={
				'usuarioNombre': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Nombre','style':'width:70%'}),
				'usuarioApellido': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Apellido','style':'width:70%'}),
				'usuarioFechaNacimiento': forms.DateInput(attrs={'required':'required','class':'form-control col-sm-4','type':'date','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'usuarioTelefono': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Telefono','style':'width:70%'}),
				'usuarioCorreo': forms.TextInput(attrs={'required':'required','class':'form-control', 'type':'email','placeholder':'Correo','style':'width:70%'}),
				}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder': 'Username','style':'width:70%'}),  
            'password': forms.PasswordInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder': 'Password','style':'width:70%'}),
        }

class LoteForm(forms.ModelForm):
	class Meta:
		model= Lote #Tabla a referenciar
		fields= ['loteFechaElaboracion','loteStock','material','loteStockReal'] #atributos a ingresar
		widgets={
				'loteFechaElaboracion': forms.DateInput(attrs={'required':'required','class':'form-control col-sm-4','type':'date','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				#'loteFechaVencimiento': forms.DateInput(attrs={'required':'required','class':'form-control col-sm-4','type':'date','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'loteStock': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','type':'number','placeholder':'Cantidad Stock','style':'width:70%'}),
				'material': forms.Select(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Material o Producto','style':'width:70%'}),
				'loteStockReal': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','type':'number','placeholder':'Cantidad Stock','style':'width:70%'}),
				}

class MaterialForm(forms.ModelForm):
	class Meta:
		model= Material #Tabla a referenciar
		fields= ['materialNombre','materialStock','materialStockMinimo','materialUnidadMedida','materialTipo','materialSubTipo','prodTermPrecio','pt'] #atributos a ingresar
		widgets={
				'materialNombre': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Nombre del material','style':'width:70%'}),
				'materialStock': forms.TextInput(attrs={'required':'required','class':'form-control','type':'number','placeholder':'Cantidad a elaborar'}),
				'materialStockMinimo': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','type':'number','placeholder':'Alerta bajo stock','style':'width:70%'}),
				'materialUnidadMedida': forms.Select(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Unidad de medida','style':'width:70%'}),
				'materialTipo': forms.Select(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Tipo de material','style':'width:70%'}),
				'materialSubTipo': forms.Select(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Subtipo de material','style':'width:70%'}),
				'prodTermPrecio': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Precio de material','style':'width:70%'}),
				'pt': forms.Select(attrs={'class':'form-control','placeholder':'Puesto de trabajo'})
				}

class ProductoForm(forms.ModelForm):
	class Meta:
		model= Material #Tabla a referenciar
		fields= ['materialNombre','materialStock','materialStockMinimo','prodTermPrecio','pt'] #atributos a ingresar
		widgets={
				'materialNombre': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Nombre Material','style':'width:70%'}),
				'materialStock': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','type':'number','placeholder':'Cantidad a elaborar (botellas)','style':'width:70%'}),
				'materialStockMinimo': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Stock Minimo Material','style':'width:70%'}),
				'prodTermPrecio': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Precio Material','style':'width:70%'}),
				'pt': forms.Select(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Puesto de trabajo','style':'width:70%'})
				}

class PTForm(forms.ModelForm):
	class Meta:
		model= PuestoDeTrabajo #Tabla a referenciar
		fields= ['ptNombre'] #atributos a ingresar
		widgets={
				'ptNombre': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Nombre del puesto de trabajo','style':'width:70%'}),
				#'materiales': forms.Select(attrs={'multiple':'multiple','class':'form-control col-sm-4','placeholder':'Materiales','style':'width:70%'})
				}

class MaquinariaForm(forms.ModelForm):
	class Meta:
		model= Maquinaria #Tabla a referenciar
		fields= ['maqNombre','maqEstado','pt'] #atributos a ingresar
		widgets={
				'maqNombre': forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'Nombre','style':'width:70%'}),
				'maqEstado': forms.Select(attrs={'required':'required','class':'form-control','placeholder':'Nombre Proveedor','style':'width:70%'}),
				'pt': forms.Select(attrs={'required':'required','class':'form-control','placeholder':'Direccion Proveedor','style':'width:70%'}),
				}

class SCForm(forms.ModelForm):
	class Meta:
		model= SolicitudDeCompra #Tabla a referenciar
		fields= ['solicitudFecha','usuario','estadoSolicitud'] #atributos a ingresar
		widgets={
				'solicitudFecha': forms.TextInput(attrs={'class':'form-control','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'usuario': forms.Select(attrs={'class':'form-control','placeholder':'Nombre Proveedor','style':'width:70%'}),
				'estadoSolicitud': forms.Select(attrs={'class':'form-control','placeholder':'Nombre Proveedor','style':'width:70%'})
				}

class DetalleSCForm(forms.ModelForm):
	class Meta:
		model= DetalleSolicitudDeCompra #Tabla a referenciar
		fields= ['detSolComCantidadProducto','solicitud','material'] #atributos a ingresar
		widgets={
				'detSolComCantidadProducto': forms.TextInput(attrs={'required':'required','class':'form-control','type':'number','placeholder':'Cantidad','style':'width:70%'}),
				'solicitud': forms.Select(attrs={'class':'form-control','placeholder':'N Solicitud de compra','style':'width:70%'}),
				'material': forms.Select(attrs={'required':'required','class':'form-control','placeholder':'Producto solicitado','style':'width:70%'})
				}			

class OFForm(forms.ModelForm):
	class Meta:
		model= OrdenDeFabricacion #Tabla a referenciar
		fields= ['ofCant','ofFechaInicio','ofFechaTermino','material','estadoOF'] #atributos a ingresar
		widgets={
				'ofCant': forms.TextInput(attrs={'required':'required','class':'form-control','type':'number','placeholder':'Cantidad','style':'width:70%'}),
				'ofFechaInicio': forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'ofFechaTermino': forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'material': forms.Select(attrs={'required':'required','class':'form-control','placeholder':'Material','style':'width:70%'}),
				'estadoOF': forms.Select(attrs={'class':'form-control','placeholder':'Estado','style':'width:70%'}),
				}

class OTForm(forms.ModelForm):
	class Meta:
		model= OrdenDeTrabajo #Tabla a referenciar
		fields= ['otFinalizacion','otFechaInicio','otFechaTermino','otCantidadAcum'] #atributos a ingresar
		widgets={
				'otFinalizacion': forms.Select(attrs={'class':'form-control','placeholder':'Estado OT','style':'width:70%'}),
				'otFechaInicio': forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'otFechaTermino': forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'otCantidadAcum': forms.TextInput(attrs={'class':'form-control','type':'number','placeholder':'Cantidad acumulada', "min":"0",'style':'width:70%'}),
				}				

class OCForm(forms.ModelForm):
	class Meta:
		model= OrdenDeCompra #Tabla a referenciar
		fields= ['ordenCompraFechaEmision','proveedor'] #atributos a ingresar
		widgets={
				'ordenCompraFechaEmision': forms.TextInput(attrs={'class':'form-control','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'proveedor': forms.Select(attrs={'required':'required','class':'form-control','placeholder':'Nombre Proveedor','style':'width:70%'})
				}

class DetalleOCForm(forms.ModelForm):
	class Meta:
		model= DetalleOrdenDeCompra #Tabla a referenciar
		fields= ['detOCCantidadMaterialSol','detOCUnidadMedidaMaterialSol','lote','ordenDeCompra'] #atributos a ingresar
		widgets={
				'detOCCantidadMaterialSol': forms.TextInput(attrs={'required':'required','class':'form-control','type':'number','placeholder':'Cantidad','style':'width:70%'}),
				'detOCUnidadMedidaMaterialSol': forms.Select(attrs={'required':'required','class':'form-control','placeholder':'N Solicitud de compra','style':'width:70%'}),
				'lote': forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'Producto solicitado','style':'width:70%'}),
				'ordenDeCompra': forms.Select(attrs={'class':'form-control','placeholder':'Producto solicitado','style':'width:70%'})
				}

class ODForm(forms.ModelForm):
	class Meta:
		model= Despacho #Tabla a referenciar
		fields= ['despachoDireccion','despachoFecha','solicitud','comuna'] #atributos a ingresar
		widgets={
				'despachoDireccion': forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'Direccion','style':'width:70%'}),
				'despachoFecha': forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'dd-mm-aaaa','style':'width:70%'}),
				'solicitud': forms.TextInput(attrs={'class':'form-control','placeholder':'N Solicitud de compra','style':'width:70%'}),
				'comuna': forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'Comuna','style':'width:70%'})
				}

class ProveedorForm(forms.ModelForm):
	class Meta:
		model= Proveedor #Tabla a referenciar
		fields= ['proveedorRut','proveedorNombre','proveedorDireccion','proveedorTelefono','proveedorCorreo'] #atributos a ingresar
		widgets={
				'proveedorRut': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Rut Proveedor','style':'width:70%'}),
				'proveedorNombre': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Nombre Proveedor','style':'width:70%'}),
				'proveedorDireccion': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Direccion Proveedor','style':'width:70%'}),
				'proveedorTelefono': forms.TextInput(attrs={'required':'required','class':'form-control col-sm-4','placeholder':'Telefono Proveedor','style':'width:70%'}),
				'proveedorCorreo': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Correo Proveedor','style':'width:70%'})
				}
