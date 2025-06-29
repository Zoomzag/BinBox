# Generated by Django 5.2.1 on 2025-05-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticulosDeLimpieza',
            fields=[
                ('id_articulo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'articulos_de_limpieza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id_log', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('accion', models.TextField(blank=True, null=True)),
                ('tabla_afectada', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bitacora',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientesVip',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('puntos', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clientes_vip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cliente', models.CharField(blank=True, max_length=100, null=True)),
                ('detalles', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'facturas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id_insumo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('unidad', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'insumos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Merma',
            fields=[
                ('id_merma', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('motivo', models.TextField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'merma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mobiliario',
            fields=[
                ('id_mob', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'mobiliario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('precio_com', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('precio_venta', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('categoria', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReStock',
            fields=[
                ('id_restock', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 're_stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'servicios',
                'managed': False,
            },
        ),
    ]
