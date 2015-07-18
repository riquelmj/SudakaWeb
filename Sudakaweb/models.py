# coding=utf-8

from django.db import models
from django.contrib.auth.models import User

Rol=(
		('Administrador','Administrador'),
		('Cliente','Cliente'),
		('Operario','Operario'),
		)

TipoMaterial=(
	('Basico','Básico'),
	('Elaborado','Elaborado'),
	)

SubTipoMaterial=(
	('Insumo','Insumo'),
	('Materia Prima','Materia Prima'),
	('Mezcla','Mezcla'),
	('Producto Terminado','Producto Terminado'),
	)

EstadoSolicitud=(
	('Pendiente','Pendiente'),
	('Aceptada','Aceptada'),
	('Rechazada','Rechazada'),
	('Cancelada','Cancelada'),
	)

EstadoMaquinaria=(
	('Activa','Activa'),
	('En Mantencion','En Mantencion'),
	('Desactivada','Desactivada'),
	)

Region=(
	('Metropolitana','Metropolitana'),
	)

Provincia=(
	('Chacabuco','Chacabuco'),
	('Cordillera','Cordillera'),
	('Maipo','Maipo'),
	('Talagante','Talagante'),
	('Melipilla','Melipilla'),
	('Santiago','Santiago'),
	)

Comuna=(
	('Colina','Colina'),
	('Lampa','Lampa'),
	('Tiltil','Tiltil'),
	('Pirque','Pirque'),
	('Puente Alto','Puente Alto'),
	('San José de Maipo','San José de Maipo'),
	('Buin','Buin'),
	('Calera de Tango','Calera de Tango'),
	('Paine','Paine'),
	('San Bernardo','San Bernardo'),
	('Alhué','Alhué'),
	('Curacaví','Curacaví'),
	('María Pinto','María Pinto'),
	('Melipilla','Melipilla'),
	('San Pedro','San Pedro'),
	('Cerrillos','Cerrillos'),
	('Cerro Navia','Cerro Navia'),
	('Conchalí','Conchalí'),
	('El Bosque','El Bosque'),
	('Estación Central','Estación Central'),
	('Huechuraba','Huechuraba'),
	('Independencia','Independencia'),
	('La Cisterna','La Cisterna'),
	('La Granja','La Granja'),
	('La Florida','La Florida'),
	('La Pintana','La Pintana'),
	('La Reina','La Reina'),
	('Las Condes','Las Condes'),
	('Lo Barnechea','Lo Barnechea'),
	('Lo Espejo','Lo Espejo'),
	('Lo Prado','Lo Prado'),
	('Macul','Macul'),
	('Maipú','Maipú'),
	('Ñuñoa','Ñuñoa'),
	('Pedro Aguirre Cerda','Pedro Aguirre Cerda'),
	('Peñalolén','Peñalolén'),
	('Providencia','Providencia'),
	('Pudahuel','Pudahuel'),
	('Quilicura','Quilicura'),
	('Quinta Normal','Quinta Normal'),
	('Recoleta','Recoleta'),
	('Renca','Renca'),
	('San Miguel','San Miguel'),
	('San Joaquín','San Joaquín'),
	('San Ramón','San Ramón'),
	('Santiago','Santiago'),
	('Vitacura','Vitacura'),
	('El Monte','El Monte'),
	('Isla de Maipo','Isla de Maipo'),
	('Padre Hurtado','Padre Hurtado'),
	('Peñaflor','Peñaflor'),
	('Talagante','Talagante'),
	)

UnidadDeMedida=(
	('kilogramos','kilogramos'),
	('gramos','gramos'),
	('litros','litros'),
	('mililitros','mililitros'),
	('centimetros cubicos','centimetros cubicos'),
	('barriles','barriles'),
	('galones','galones'),
	('botellas','botellas'),
	('sacos','sacos'),
	('cajas','cajas'),
	('unidades','unidades'),
	)

PUESTO_DE_TRABAJO=(
				  ('Coccion','Obtención de mosto'),
				  ('Fermentación','Fermentación'),
			      ('Envasado','Envasado'),
				  ('Embotellado','Embotellado'),
				  )

ESTADO_OF=(
	      ('Pendiente','Pendiente'),
	      ('En Proceso','En Proceso'),
	      ('Finalizada','Finalizada'),
	      ('Cancelada','Cancelada'),
	      )


Habilitador=(
				 ("1",'Habilitado'),
				 ("0",'Inhabilitado'),
				 )

Finalizacion=(
				 ('Pendiente','Pendiente'),
				 ('Por iniciar','Por iniciar'),
				 ('Iniciada','Iniciada'),
				 ('Finalizada','Finalizada'),
				 )


## ENTIDAD USUARIO
class Usuario(models.Model):	
	id= models.AutoField('id',primary_key=True)
	usuarioNombre = models.CharField('Nombre del usuario',max_length=50,null = False, blank=False)
	usuarioApellido = models.CharField('Apellido del usuario',max_length=50,null = False, blank=False)	
	usuarioFechaNacimiento=models.DateField('Fecha de nacimiento del Usuario')
	usuarioTelefono=models.IntegerField('Numero telefonico del Usuario')
	usuarioCorreo=models.EmailField('Correo electronico del usuario')
	usuarioHabilitador=models.NullBooleanField('Habilitador del usuario', choices=Habilitador, null=False, blank=False)
	usuarioRol=models.CharField('Rol del usuario',max_length=50,null=False,blank=False, choices=Rol)

		#llave foranea Relación uno a unocon la tabla usuario del sistema
	user = models.OneToOneField(User, null=True, blank=True)

	def __unicode__(self):
		return u'%s %s, Rol: %s'% (self.usuarioNombre,self.usuarioApellido,self.usuarioRol)


## ENTIDAD ESTADO SOLICITUD DE COMPRA
class EstadoSolicitud(models.Model):
	id=models.AutoField('id',primary_key=True)
	estadoNombre=models.CharField('Nombre del estado de la solicitud de compra',max_length=50,null=False,blank=False, choices=EstadoSolicitud)

	def __unicode__(self):
		return u'%s'%(self.estadoNombre)


## ENTIDAD REGIÓN
class Region(models.Model):
	id= models.AutoField('id',primary_key=True)
	regionNombre=models.CharField('Nombre de la region',max_length=50,null=False,blank=False, choices=Region)

	def __unicode__(self):
		return u'%s'%(self.regionNombre)


## ENTIDAD PROVINCIA
class Provincia(models.Model):
	id= models.AutoField('id',primary_key=True)
	provinciaNombre=models.CharField('Nombre de provincia',max_length=50,null=False,blank=False, choices=Provincia)

	# llave foranea
	region=models.ForeignKey(Region,verbose_name="Region")

	def __unicode__(self):
		return u'%s'%(self.provinciaNombre)


## ENTIDAD COMUNA
class Comuna(models.Model):
	id= models.AutoField('id',primary_key=True)
	comunaNombre=models.CharField('Nombre de la comuna',max_length=50,null=False,blank=False, choices=Comuna)

	# llave foranea
	provincia=models.ForeignKey(Provincia,verbose_name="Provincia")

	def __unicode__(self):
		return u'%s'%(self.comunaNombre)



## ENTIDAD SOLICITUD DE COMPRA
class SolicitudDeCompra(models.Model):
	id=models.AutoField('id',primary_key=True)
	solicitudFecha=models.DateField('Fecha cuando se emitio la solicitud', db_index=True)

	#llave foraneas
	usuario=models.ForeignKey(Usuario,verbose_name="Usuario")
	estadoSolicitud=models.ForeignKey(EstadoSolicitud,verbose_name="Estado Solicitud")

	def __unicode__(self):
		return u'%s - Solicitado por: %s'%(self.id,self.usuario)


# ENTIDAD DESPACHO
class Despacho(models.Model):
	id = models.AutoField('id',primary_key=True)
	despachoDireccion=models.CharField('Dirección de despacho',max_length=50,null=False,blank=False)
	despachoFecha=models.DateField('Fecha del despacho')

	# llaves foraneas
	solicitud=models.ForeignKey(SolicitudDeCompra,verbose_name="Solicitud de compra")
	comuna=models.ForeignKey(Comuna,verbose_name="Comuna")

	def __unicode__(self):
		return u'%s %s, n° SC: %s'%(self.despachoDireccion,self.despachoFecha,self.solicitud)


## ENTIDAD MATERIAL
class Material(models.Model):
	id=models.AutoField('id',primary_key=True)
	materialNombre=models.CharField('Nombre del material',max_length=50,null=False,blank=False)
	materialStock=models.FloatField('Cantidad a elaborar',null=True,blank=True)
	materialStockMinimo=models.FloatField('Stock minimo de los materiales',null=False,blank=False)
	materialUnidadMedida=models.CharField('Unidades de medidas de los materiales',max_length=50,null=False,blank=False, choices=UnidadDeMedida)
	materialTipo=models.CharField('Tipo de Material(Basico o Compuesto)',max_length=50,null=False,blank=False, choices=TipoMaterial)
	materialSubTipo=models.CharField('Sub tipo de Material Compuesto (SemiElaborado o Producto Terminado)',max_length=50,null=False,blank=False, choices=SubTipoMaterial)
	prodTermPrecio=models.IntegerField('Precio del producto terminado',null=True,blank=True)
	materialTiempoCaducidad = models.IntegerField('Meses de caducidad', null=False, blank=False)

	# llave foranea
	pt=models.ForeignKey('PuestoDeTrabajo',verbose_name="Puesto de Trabajo", blank=True, null=True)

	def __unicode__(self):
		return u'%s'%(self.materialNombre)


## ENTIDAD PUESTO DE TRABAJO
class PuestoDeTrabajo(models.Model):
	id=models.AutoField('id',primary_key=True)
	ptNombre=models.CharField('Nombre del puesto de trabajo',max_length=50,null=False,blank=False)

	# llave foranea	
	materiales = models.ManyToManyField(Material)

	def __unicode__(self):
		return u'%s'%(self.ptNombre)


## ENTIDAD DETALLE SOLICITUD DE COMPRA
class DetalleSolicitudDeCompra(models.Model):
	detSolComCantidadProducto=models.IntegerField('Cantidad de producto solicitado',null=False,blank=False)

	# llaves foraneas
	solicitud=models.ForeignKey(SolicitudDeCompra,verbose_name="Solicitud de compra")
	material=models.ForeignKey(Material,verbose_name="Material")

	def __unicode__(self):
		return u'%s, Cantidad: %s'%(self.material,self.detSolComCantidadProducto)


## ENTIDAD COMPOSICIÓN
class Composicion(models.Model):
	composicionCantidad=models.FloatField('Cantidad de composición que tiene cada material',null=False,blank=False)

	# llaves foraneas
	material1=models.ForeignKey('Material',verbose_name="Material 1",related_name='material1')
	material2=models.ForeignKey('Material',verbose_name="Material 2",related_name='material2')

	def __unicode__(self):
		return u'%s, Cantidad: %s'% (self.material1,self.composicionCantidad)


## ENTIDAD LOTE
class Lote(models.Model):
	id=models.AutoField('id',primary_key=True)
	loteFechaElaboracion=models.DateField('Fecha de elaboración del lote de material')
	loteFechaVencimiento=models.DateField('Fecha de Vencimiento de los lotes de material', db_index=True, null=True, blank=True)
	loteStock=models.IntegerField('Cantidad total de materiales',null=False,blank=False)
	loteStockReal=models.IntegerField('Stock actual del lote',null=False,blank=False)

	# llave foranea
	material=models.ForeignKey(Material,verbose_name="Material", db_index=True)

	def __unicode__(self):
		return u'%s, Stock: %s, Elab: %s,  Venc: %s' % (self.material,self.loteStock,self.loteFechaElaboracion,self.loteFechaVencimiento)

	class Meta:
		ordering=['loteFechaVencimiento','material']


## ENTIDAD PROVEEDOR
class Proveedor(models.Model):
	id=models.AutoField('id',primary_key=True)
	proveedorRut=models.CharField('Rut del proveedor',max_length=20,null=False,blank=False)
	proveedorNombre=models.CharField('Nombre del proveedor',max_length=50,null=False,blank=False)
	proveedorDireccion=models.CharField('Dirección del proveedor',max_length=50,null=False,blank=False)
	proveedorTelefono=models.IntegerField('Telefono del proveedor',null=False,blank=False)
	proveedorCorreo=models.EmailField('Correo electronico del proveedor')

	def __unicode__(self):
		return u'%s' %(self.proveedorNombre)


## ENTIDAD ORDEN DE COMPRA
class OrdenDeCompra(models.Model):
	id=models.AutoField('id',primary_key=True)
	ordenCompraFechaEmision=models.DateField('Fecha de emisión de la orden de compra')

	#llave foranea
	proveedor=models.ForeignKey(Proveedor,verbose_name="Proveedor")

	def __unicode__(self):
		return u'%s, Emision: %s'%(self.id,self.ordenCompraFechaEmision)


## ENTIDAD DETALLE ORDEN DE COMPRA
class DetalleOrdenDeCompra(models.Model):
	detOCCantidadMaterialSol=models.IntegerField('Cantidad de material a solicitar al comprador',null=False,blank=False)
	detOCUnidadMedidaMaterialSol=models.CharField('Unidad de medida del material a comprar',max_length=50,null=False,blank=False)

	#llaves foraneas
	lote=models.ForeignKey(Lote,verbose_name="Lote")
	ordenDeCompra=models.ForeignKey(OrdenDeCompra,verbose_name="Orden de Compra")

	def __unicode__(self):
		return u'%s, Cant: %s %s'%(self.lote,self.detOCCantidadMaterialSol,self.detOCUnidadMedidaMaterialSol)


## ENTIDAD ESTADO ORDEN DE FABRICACIÓN
class EstadoOF(models.Model):
	id=models.AutoField('id',primary_key=True)
	estadoOFNombre=models.CharField('Nombre del estado de la orden de fabricación',max_length=50,null=False,blank=False)

	def __unicode__(self):
		return u'%s' %(self.estadoOFNombre)

## ENTIDAD ORDEN DE FABRICACIÓN
class OrdenDeFabricacion(models.Model):
	id=models.AutoField('id',primary_key=True)
	ofCant=models.IntegerField('Cantidad a fabricar',null=False,blank=False)
	ofFechaIngreso=models.DateField('Fecha de ingreso de la OF', db_index=True, null=True, blank=True)
	ofFechaInicio=models.DateField('Fecha de inicio de la OF')	
	ofFechaTermino=models.DateField('Fecha de termino de la OF')


	#llaves foraneas	
	material=models.ForeignKey(Material, db_index=True, verbose_name="Material")
	usuario=models.ForeignKey(Usuario,verbose_name="Usuario", null=True, blank=True)
	estadoOF=models.CharField("Estado OF", max_length=20,choices=ESTADO_OF, null=True, blank=True)

	def __unicode__(self):
		return u'n° OF: %s'%(self.id)
	
	class Meta:
		ordering=['ofFechaIngreso']


## ENTIDAD ETAPA
class Etapa(models.Model):
	id=models.AutoField('id',primary_key=True)
	etapaNombre=models.CharField('Nombre de la etapa',max_length=50,null=False,blank=False)

	#llaves foraneas	
	#material = models.ForeignKey(Material,verbose_name="Material")
	materiales = models.TextField('Lista de materiales',max_length=1000,null=True,blank=True)
	pt1 = models.ForeignKey(PuestoDeTrabajo,verbose_name="PT1")
	siguiente = models.ForeignKey('self',verbose_name='Siguiente', null=True, blank=True)
	#pt2=models.ForeignKey(PuestoDeTrabajo,verbose_name="PT2")

	def __unicode__(self):
		return u'%s %s'%(self.etapaNombre,self.pt1)


## ENTIDAD ORDEN DE TRABAJO
class OrdenDeTrabajo(models.Model):
	id=models.AutoField('id',primary_key=True)
	otFinalizacion=models.CharField('Estado OT',max_length=50, choices=Finalizacion, null=False, blank=False)
	otFechaInicio=models.DateField('Fecha de inicio de la OT', null=True, blank=True)
	otFechaTermino=models.DateField('Fecha de termino de la OT', null=True, blank=True)
	otCantidad=models.IntegerField('Cantidad total a fabricar', null=False, blank=False)
	otCantidadAcum=models.IntegerField('Cantidad acumulada', null=False, blank=False)

	#llaves foraneas
	of=models.ForeignKey(OrdenDeFabricacion,verbose_name="OF", db_index=True)
	pt=models.ForeignKey(PuestoDeTrabajo,verbose_name="PT", db_index=True)
	material=models.ForeignKey(Material,verbose_name="Material", db_index=True)

	def __unicode__(self):
		return u'n° OT: %s, Estado: %s, %s'%(self.id,self.otFinalizacion,self.of)


## ENTIDAD MAQUINARIA
class Maquinaria(models.Model):
	id=models.AutoField('id',primary_key=True)
	maqNombre=models.CharField('Nombre de la maquina',max_length=50,null=False,blank=False)
	maqEstado=models.CharField('Estado de la maquina',max_length=50,null=False,blank=False, choices=EstadoMaquinaria)

	#llave foranea	
	pt=models.ForeignKey(PuestoDeTrabajo,verbose_name="PT")

	def __unicode__(self):
		return u'%s - %s'%(self.maqNombre,self.maqEstado)


## ENTIDAD NOTIFICACIÓN
class Notificacion(models.Model):
	id=models.AutoField('id',primary_key=True)
	notifDescripcion=models.CharField('Descripción de la notificación',max_length=200,null=False,blank=False)
	notifFecha=models.DateField('Fecha de notificación')
	notifCantidad=models.IntegerField('Cantidad de material que se entrega en la notificación',null=False,blank=False)

	# llaves foraneas
	usuario=models.ForeignKey(Usuario,verbose_name="Usuario",null=True)
	ot=models.ForeignKey(OrdenDeTrabajo,verbose_name="OT")

	def __unicode__(self):
		return u'%s, Cant: %s'%(self.notifDescripcion,self.notifCantidad)
	

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
	auditoriaFechaModificacion= models.DateField('Fecha de Modificacion',auto_now=True) 
	auditoriaTablaModificada= models.CharField('Tabla Modificada', max_length=50, null=False, blank=False)
	auditoriaDatosAntes= models.CharField('Datos Antes', max_length=128, null=False, blank=False)
	auditoriaDatosDespues= models.CharField('Datos Despues', max_length=128, null=False, blank=False)
	auditoriaOperacion= models.CharField('Operacion', max_length=50, null=False, blank=False)

	#Llave Foranea
	usuario= models.ForeignKey(Usuario,verbose_name="Usuario")

	def __unicode__(self):
		return u'%s%s%s'%(self.auditoriaTablaModificada,self.auditoriaFechaModificacion,auditoriaOperacion)
		