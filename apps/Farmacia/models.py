# Nombre del archivo: models.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/urls.py
# Objetivo: Proveer los modelos de la aplicacion Farmacia
# Comentarios: NO TOCAR LOS MODELOS DE LA APLICACION Farmacia

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Descuento(models.Model):
    id_descuento = models.IntegerField(db_column='ID_DESCUENTO', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='NOMBRE')  # Field name made lowercase.
    field_desc = models.IntegerField(db_column='_DESC')  # Field name made lowercase. Field renamed because it started with '_'.
    fecha_inicio = models.DateField(db_column='FECHA_INICIO')  # Field name made lowercase.
    fecha_fin = models.DateField(db_column='FECHA_FIN')  # Field name made lowercase.

    class Meta:
        db_table = 'DESCUENTO'


class Devolucion(models.Model):
    id_devolucion = models.IntegerField(db_column='ID_DEVOLUCION', primary_key=True)  # Field name made lowercase.
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='ID_VENTA', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL')  # Field name made lowercase.
    fecha_devolucion = models.DateField(db_column='FECHA_DEVOLUCION')  # Field name made lowercase.

    class Meta:
        db_table = 'DEVOLUCION'


class DevolucionMed(models.Model):
    id_devolucion_det = models.IntegerField(db_column='ID_DEVOLUCION_DET', primary_key=True)  # Field name made lowercase.
    id_devolucion = models.ForeignKey(Devolucion, models.DO_NOTHING, db_column='ID_DEVOLUCION', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='CANTIDAD')  # Field name made lowercase.
    precio_unitario = models.FloatField(db_column='PRECIO_UNITARIO')  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL')  # Field name made lowercase.

    class Meta:
        db_table = 'DEVOLUCION_MED'


class Empresa(models.Model):
    id_empresa = models.IntegerField(db_column='ID_EMPRESA', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='NOMBRE')  # Field name made lowercase.

    class Meta:
        db_table = 'EMPRESA'


class Kardex(models.Model):
    id_transaccion = models.IntegerField(db_column='ID_TRANSACCION', primary_key=True)  # Field name made lowercase.
    id_ope = models.ForeignKey('TipoOperacion', models.DO_NOTHING, db_column='ID_OPE')  # Field name made lowercase.
    id_medic = models.IntegerField(db_column='ID_MEDIC')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    precio_unitario = models.FloatField(db_column='PRECIO_UNITARIO')  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL')  # Field name made lowercase.

    class Meta:
        db_table = 'KARDEX'


class Lote(models.Model):
    id_lote = models.IntegerField(db_column='ID_LOTE', primary_key=True)  # Field name made lowercase.
    id_medicamento = models.ForeignKey('Medicamento', models.DO_NOTHING, db_column='ID_MEDICAMENTO', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='ID_EMPRESA', blank=True, null=True)  # Field name made lowercase.
    fecha_compra = models.DateField(db_column='FECHA_COMPRA', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'LOTE'


class Medicamento(models.Model):
    id_medicamento = models.IntegerField(db_column='ID_MEDICAMENTO', primary_key=True)  # Field name made lowercase.
    id_presentacion = models.ForeignKey('Presentacion', models.DO_NOTHING, db_column='ID_PRESENTACION')  # Field name made lowercase.
    id_tipo = models.ForeignKey('TipoMedicamento', models.DO_NOTHING, db_column='ID_TIPO')  # Field name made lowercase.
    nombre = models.TextField(db_column='NOMBRE')  # Field name made lowercase.
    precio = models.FloatField(db_column='PRECIO')  # Field name made lowercase.

    class Meta:
        db_table = 'MEDICAMENTO'


class Presentacion(models.Model):
    id_presentacion = models.IntegerField(db_column='ID_PRESENTACION', primary_key=True)  # Field name made lowercase.
    presentacion = models.TextField(db_column='PRESENTACION')  # Field name made lowercase.

    class Meta:
        db_table = 'PRESENTACION'


class Rol(models.Model):
    id_rol = models.IntegerField(db_column='ID_ROL', primary_key=True)  # Field name made lowercase.
    rol = models.TextField(db_column='ROL')  # Field name made lowercase.

    class Meta:
        db_table = 'ROL'


class TipoMedicamento(models.Model):
    id_tipo = models.IntegerField(db_column='ID_TIPO', primary_key=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='TIPO')  # Field name made lowercase.

    class Meta:
        db_table = 'TIPO_MEDICAMENTO'


class TipoOperacion(models.Model):
    id_ope = models.IntegerField(db_column='ID_OPE', primary_key=True)  # Field name made lowercase.
    operacion = models.CharField(db_column='OPERACION', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'TIPO_OPERACION'


class User(AbstractUser):
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='ID_EMPRESA',null=True)  # Field name made lowercase.
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='ID_ROL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'USER'


class Venta(models.Model):
    id_venta = models.IntegerField(db_column='ID_VENTA', primary_key=True)  # Field name made lowercase.
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='ID_USER', blank=True, null=True)  # Field name made lowercase.
    field_desc = models.IntegerField(db_column='_DESC')  # Field name made lowercase. Field renamed because it started with '_'.
    fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL')  # Field name made lowercase.

    class Meta:
        db_table = 'VENTA'


class VentaMed(models.Model):
    id_venta_detalle = models.IntegerField(db_column='ID_VENTA_DETALLE', primary_key=True)  # Field name made lowercase.
    id_venta = models.ForeignKey(Venta, models.DO_NOTHING, db_column='ID_VENTA', blank=True, null=True)  # Field name made lowercase.
    id_medicamento = models.ForeignKey(Medicamento, models.DO_NOTHING, db_column='ID_MEDICAMENTO', blank=True, null=True)  # Field name made lowercase.
    id_descuento = models.ForeignKey(Descuento, models.DO_NOTHING, db_column='ID_DESCUENTO', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    precio_neto = models.FloatField(db_column='PRECIO_NETO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'VENTA_MED'
