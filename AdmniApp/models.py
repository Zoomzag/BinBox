from django.db import models

class ArticulosDeLimpieza(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articulos_de_limpieza'

 

class Bitacora(models.Model):
    id_log = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    accion = models.TextField(blank=True, null=True)
    tabla_afectada = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacora'


class ClientesVip(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    puntos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_vip'


class Facturas(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    detalles = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturas'


class Insumos(models.Model):
    id_insumo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insumos'


class Merma(models.Model):
    id_merma = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    motivo = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merma'


class Mobiliario(models.Model):
    id_mob = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobiliario'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_com = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class ReStock(models.Model):
    id_restock = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 're_stock'


class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'
