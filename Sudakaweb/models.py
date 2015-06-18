# coding=utf-8


from django.db import models
from django.contrib.auth.models import User

USUARIO=(
		('Administrador','Administrador'),
		('Cliente','Cliente'),
		('Operario','Operario'),
		)

MATERIAL=(
		 ('agua','agua'),
		 ('cebada','cebada'),
		 ('lúpudo','lúpudo'),
		 ('levadura','levadura'),
		 ('malteros','malteros'),
		 ('mostos','mostos'),
		 ('malta','malta'),
		 ('amilasa','amilasa'),
		 ('grits','grits'),
		 ('trigo','trigo'),
		 ('avena','avena'),
		 ('maíz','maíz'),
		 ('azúcar','azúcar'),
		 ('botella','botella'),
		 ('tapa','tapa'),
		 ('caja','caja'),
		 ('logo','logo'),
		 ('cerveza lager','cerveza lager'),
		 ('cerveza ale','cerveza ale'),
		 ('cerveza negra','cerveza negra'),
		 )

MAQUINARIA=(
		   ('maquina1','maquina1'),
		   ('maquina2','maquina2'),
		   ('maquina3','maquina3'),
		   ('maquina4','maquina4'),
		   ('maquina5','maquina5'),
		   ('maquina6','maquina6'),
		   )

ESTADO=(
	   ('aceptado','aceptado'),
	   ('rechazado','rechazado'),
	   ('pendiente','pendiente'),
	   )

PUESTO_DE_TRABAJO=(
				  ('Coccion','Obtención de mosto'),
				  ('Fermentación','Fermentación'),
			      ('Envasado','Envasado'),
				  ('Embotellado','Embotellado'),
				  )

ESTADO_OF=(
	      ('en proceso','en proceso'),
	      ('eliminado','eliminado'),
	      ('en espera','en espera'),
	      ('culminada','culminada'),
	      )

ORDEN_DE_TRABAJO=(
				 ('Orden de trabajo cerveza lager','Orden de trabajo cerveza lager'),
				 ('Orden de trabajo cerveza black','Orden de trabajo cerveza black'),
				 ('Orden de trabajo cerveza rubia','Orden de trabajo cerveza rubia'),
				 )


## ENTIDAD USUARIO
class Usuario(models.Model):	
	id= models.AutoField('id',primary_key=True)
	usuarioNombre = models.CharField('Nombre del usuario',max_length=50,null = False, blank=False)
	usuarioApellido = models.CharField('Apellido del usuario',max_length=50,null = False, blank=False)	
	usuarioFechaNacimiento=models.DateField('Fecha de nacimiento del Usuario')
	usuarioTelefono=models.IntegerField('Numero telefonico del Usuario',null=False,blank=False)
	usuarioCorreo=models.EmailField('Correo electronico del usuario')
	usuarioClave=models.CharField('Clave de ingreso del usuario',max_length=50,null=False,blank=False)
	usuarioHabilitador=models.NullBooleanField('Habilitador del usuario')
	usuarioRol=models.CharField('Rol del usuario',max_length=50,null=False,blank=False)

		#llave foranea Relación uno a unocon la tabla usuario del sistema
	user = models.OneToOneField(User)

	def __unicode__(self):
		return u'%s%s%s'% (self.usuarioNombre,self.usuarioApellido,self.usuarioRol)


## ENTIDAD ESTADO
class Estado(models.Model):
	id=models.AutoField('id',primary_key=True)
	estadoNombre=models.CharField('Nombre del estado',max_length=50,null=False,blank=False)

	def __unicode__(self):
		return u'%s'%(self.estadoNombre)


## ENTIDAD REGIÓN
class Region(models.Model):
	id= models.AutoField('id',primary_key=True)
	regionNombre=models.CharField('Nombre de la region',max_length=50,null=False,blank=False)

	def __unicode__(self):
		return u'%s'%(self.regionNombre)


## ENTIDAD CIUDAD
class Ciudad(models.Model):
	id= models.AutoField('id',primary_key=True)
	ciudadNombre=models.CharField('Nombre de ciudad',max_length=50,null=False,blank=False)

	# llave foranea
	region=models.ForeignKey(Region,verbose_name="Region")

	def __unicode__(self):
		return u'%s'%(self.ciudadNombre)


## ENTIDAD COMUNA
class Comuna(models.Model):
	id= models.AutoField('id',primary_key=True)
	comunaNombre=models.CharField('Nombre de la comuna',max_length=50,null=False,blank=False)

	# llave foranea
	ciudad=models.ForeignKey(Ciudad,verbose_name="Ciudad")

	def __unicode__(self):
		return u'%s'%(self.comunaNombre)



## ENTIDAD SOLICITUD DE COMPRA
class SolicitudDeCompra(models.Model):
	id=models.AutoField('id',primary_key=True)
	solicitudFecha=models.DateField('Fecha cuando se emitio la solicitud')

	#llave foraneas
	usuario=models.ForeignKey(Usuario,verbose_name="Usuario")
	estado=models.ForeignKey(Estado,verbose_name="Estado")

	def __unicode__(self):
		return u'%s%s'%(self.solicitudFecha,self.usuario)


# ENTIDAD DESPACHO
class Despacho(models.Model):
	id = models.AutoField('id',primary_key=True)
	despachoDireccion=models.CharField('Dirección de despacho',max_length=50,null=False,blank=False)
	despachoFecha=models.DateField('Fecha del despacho')

	# llaves foraneas
	solicitud=models.ForeignKey(SolicitudDeCompra,verbose_name="Solicitud de compra")
	comuna=models.ForeignKey(Comuna,verbose_name="Comuna")

	def __unicode__(self):
		return u'%s%s%s'%(self.despachoDireccion,self.despachoFecha,self.solicitud)



## ENTIDAD PUESTO DE TRABAJO
class PuestoDeTrabajo(models.Model):
	id=models.AutoField('id',primary_key=True)
	ptNombre=models.CharField('Nombre del puesto de trabajo',max_length=50,null=False,blank=False)

	# llave foranea	
	usuario=models.ForeignKey(Usuario,verbose_name="Usuario")

	def __unicode__(self):
		return u'%s%s'%(self.ptNombre,self.usuario)

## ENTIDAD MATERIAL
class Material(models.Model):
	id=models.AutoField('id',primary_key=True)
	materialNombre=models.CharField('Nombre del material',max_length=50,null=False,blank=False)
	materialStock=models.IntegerField('Stock del material',null=False,blank=False)
	materialStockMinimo=models.IntegerField('Stock minimo de los materiales',null=False,blank=False)
	materialUnidadMedida=models.CharField('Unidades de medidas de los materiales',max_length=50,null=False,blank=False)
	materialTipo=models.CharField('Tipo de Material(Basico o Compuesto)',max_length=50,null=False,blank=False)
	materialSubTipo=models.CharField('Sub tipo de Material Compuesto (SemiElaborado o Producto Terminado)',max_length=50,null=False,blank=False)
	prodTermPrecio=models.IntegerField('Precio del producto terminado',null=False,blank=False)

	# llave foranea
	pt=models.ForeignKey(PuestoDeTrabajo,verbose_name="Puesto de Trabajo")

	def __unicode__(self):
		return u'%s%s'%(self.Material_Nombre,self.Material_Stock)


## ENTIDAD DETALLE SOLICITUD DE COMPRA
class DetalleSolicitudDeCompra(models.Model):
	detSolComCantidadProducto=models.IntegerField('Cantidad de producto solicitado',null=False,blank=False)

	# llaves foraneas
	solicitud=models.ForeignKey(SolicitudDeCompra,verbose_name="Solicitud de compra")
	material=models.ForeignKey(Material,verbose_name="Material")

	def __unicode__(self):
		return u'%s%s'%(self.material,self.detSolComCantidadProducto)


## ENTIDAD COMPOSICIÓN
class Composicion(models.Model):
	composicionCantidad=models.IntegerField('Cantidad de composición que tiene cada material',null=False,blank=False)

	# llaves foraneas
	material1=models.ForeignKey(Material,verbose_name="Material 1")
	#material2=models.ForeignKey(Material,verbose_name="Material 2")

	def __unicode__(self):
		return u'%s%s'% (self.material,self.composicionCantidad)


## ENTIDAD LOTE
class Lote(models.Model):
	id=models.AutoField('id',primary_key=True)
	loteFechaElaboracion=models.DateField('Fecha de elaboración del lote de material')
	loteFechaVencimiento=models.DateField('Fecha de Vencimiento de los lotes de material')
	loteStock=models.IntegerField('Stock del lote de materiales',null=False,blank=False)

	# llave foranea
	material=models.ForeignKey(Material,verbose_name="Material")

	def __unicode__(self):
		return u'%s%s%s%s' % (self.material,self.loteFechaElaboracion,self.loteStock,self.loteFechaVencimiento)

	class Meta:
		ordering=['loteFechaVencimiento','material']


## ENTIDAD PROVEEDOR
class  Proveedor(models.Model):
	id=models.AutoField('id',primary_key=True)
	proveedorRut=models.IntegerField('Rut del proveedor',max_length=20,null=False,blank=False)
	proveedorNombre=models.CharField('Nombre del proveedor',max_length=50,null=False,blank=False)
	proveedorDireccion=models.CharField('Dirección del proveedor',max_length=50,null=False,blank=False)
	proveedorTelefono=models.IntegerField('Telefono del proveedor',null=False,blank=False)
	proveedorCorreo=models.EmailField('Correo electronico del proveedor')

	def __unicode__(self):
		return u'%s%s' %(self.proveedorNombre,self.proveedorCorreo)


## ENTIDAD ORDEN DE COMPRA
class OrdenDeCompra(models.Model):
	id=models.AutoField('id',primary_key=True)
	ordenCompraFechaEmision=models.DateField('Fecha de emisión de la orden de compra')

	#llave foranea
	proveedor=models.ForeignKey(Proveedor,verbose_name="Proveedor")

	def __unicode__(self):
		return u'%s%s'%(self.id,self.ordenCompraFechaEmision)


## ENTIDAD DETALLE ORDEN DE COMPRA
class DetalleOrdenDeCompra(models.Model):
	detOCCantidadMaterialSol=models.IntegerField('Cantidad de material a solicitar al comprador',null=False,blank=False)
	detOCUnidadMedidaMaterialSol=models.CharField('Unidad de medida del material a comprar',max_length=50,null=False,blank=False)

	#llaves foraneas
	lote=models.ForeignKey(Lote,verbose_name="Lote")
	ordenDeCompra=models.ForeignKey(OrdenDeCompra,verbose_name="Orden de Compra")

	def __unicode__(self):
		return u'%s%s%s'%(self.lote,self.detOCCantidadMaterialSol,self.detOCUnidadMedidaMaterialSol)


## ENTIDAD ESTADO ORDEN DE FABRICACIÓN
class EstadoOF(models.Model):
	id=models.AutoField('id',primary_key=True)
	estadoOFNombre=models.CharField('Nombre del estado de la orden de fabricación',max_length=50,null=False,blank=False)

	def __unicode__(self):
		return u'%s%s' %(self.id,self.estadoOFNombre)

## ENTIDAD ORDEN DE FABRICACIÓN
class OrdenDeFabricacion(models.Model):
	id=models.AutoField('id',primary_key=True)
	ofCant=models.IntegerField('Cantidad de a Fabricar en la orden de fabricación',null=False,blank=False)
	ofFechaInicio=models.DateField('Fecha de inicio de la orden de fabricación')	
	ofFechaTermino=models.DateField('Fecha de termino de la orden de fabricación')
	ofFechaIngreso=models.DateField('Fecha de ingreso de la orden de fabricación')

	#llaves foraneas	
	material=models.ForeignKey(Material,verbose_name="Material")
	usuario=models.ForeignKey(Usuario,verbose_name="Usuario")
	estadoOF=models.ForeignKey(EstadoOF,verbose_name="Estado OF")

	def __unicode__(self):
		return u'%s%s%s%s'%(self.id,self.material,self.ofCant,self.ofFechaIngreso)
	
	class Meta:
		ordering=['ofFechaIngreso']


## ENTIDAD ETAPA
class Etapa(models.Model):
	id=models.AutoField('id',primary_key=True)
	etapaNombre=models.CharField('Nombre de la etapa',max_length=50,null=False,blank=False)

	#llaves foraneas	
	material=models.ForeignKey(Material,verbose_name="Material")
	pt1=models.ForeignKey(PuestoDeTrabajo,verbose_name="PT1")
	#pt2=models.ForeignKey(PuestoDeTrabajo,verbose_name="PT2")

	def __unicode__(self):
		return u'%s%s%s'%(self.etapaNombre,self.pt1,self.pt2)


## ENTIDAD ORDEN DE TRABAJO
class OrdenDeTrabajo(models.Model):
	id=models.AutoField('id',primary_key=True)
	otFinalizacion=models.NullBooleanField('Estado orden de trabajo finalizado o no')
	otFechaInicio=models.DateField('Fecha de inicio de la orden de trabajo')
	otFechaTermino=models.DateField('Fecha de termino de la orden de trabajo')

	#llaves foraneas
	of=models.ForeignKey(OrdenDeFabricacion,verbose_name="OF")
	etapa=models.ForeignKey(Etapa,verbose_name="Etapa")
	pt=models.ForeignKey(PuestoDeTrabajo,verbose_name="PT")

	def __unicode__(self):
		return u'%s%s%s'%(self.id,self.otFinalizacion,self.of)


## ENTIDAD MAQUINARIA
class Maquinaria(models.Model):
	id=models.AutoField('id',primary_key=True)
	maqNombre=models.CharField('Nombre de la maquina',max_length=50,null=False,blank=False)
	maqEstado=models.CharField('Estado de la maquina',max_length=50,null=False,blank=False)

	#llave foranea	
	pt=models.ForeignKey(PuestoDeTrabajo,verbose_name="PT")

	def __unicode__(self):
		return u'%s%s'%(self.maqNombre,self.maqEstado)


## ENTIDAD NOTIFICACIÓN
class Notificacion(models.Model):
	id=models.AutoField('id',primary_key=True)
	notifDescripcion=models.CharField('Descripción de la notificación',max_length=200,null=False,blank=False)
	notifFecha=models.DateField('Fecha de notificación')
	notifCantidad=models.IntegerField('Cantidad de material que se entrega en la notificación',null=False,blank=False)

	# llaves foraneas
	usuario=models.ForeignKey(Usuario,verbose_name="Usuario")
	ot=models.ForeignKey(OrdenDeTrabajo,verbose_name="OT")

	def __unicode__(self):
		return u'%s%s%s'%(self.id,self.notifDescripcion,self.notifCantidad)
	

## ENTIDAD CONSUMO
class Consumo(models.Model):
	consumoCantidad=models.IntegerField('Cantidad que se consumio',null=False,blank=False)
	consumoUnidadMedida=models.CharField('Unidad de medida del producto saliente',max_length=50,null=False,blank=False)

	#llaves foraneas	
	notificacion=models.ForeignKey(Notificacion,verbose_name="Notificacion")
	lote=models.ForeignKey(Lote,verbose_name="Lote")

	def __unicode__(self):
		return u'%s%s'%(self.lote,self.consumoCantidad)


## AUDITORIA
class Auditoria(models.Model):
	id= models.AutoField('id',primary_key=True)
	auditoriaFechaModificacion= models.DateField('Fecha de Modificacion') 
	auditoriaTablaModificada= models.CharField('Tabla Modificada', max_length=50, null=False, blank=False)
	auditoriaDatosAntes= models.CharField('Datos Antes', max_length=128, null=False, blank=False)
	auditoriaDatosDespues= models.CharField('Datos Despues', max_length=128, null=False, blank=False)
	auditoriaOperacion= models.CharField('Operacion', max_length=50, null=False, blank=False)

	#Llave Foranea
	usuario= models.ForeignKey(Usuario,verbose_name="Usuario")

	def __unicode__(self):
		return u'%s%s%s'%(self.auditoriaTablaModificada,self.auditoriaFechaModificacion,auditoriaOperacion)
		