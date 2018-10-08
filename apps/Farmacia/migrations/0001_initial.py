# Generated by Django 2.1.2 on 2018-10-08 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id_descuento', models.IntegerField(db_column='ID_DESCUENTO', primary_key=True, serialize=False)),
                ('nombre', models.TextField(db_column='NOMBRE')),
                ('field_desc', models.IntegerField(db_column='_DESC')),
                ('fecha_inicio', models.DateField(db_column='FECHA_INICIO')),
                ('fecha_fin', models.DateField(db_column='FECHA_FIN')),
            ],
            options={
                'db_table': 'DESCUENTO',
            },
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id_devolucion', models.IntegerField(db_column='ID_DEVOLUCION', primary_key=True, serialize=False)),
                ('total', models.FloatField(db_column='TOTAL')),
                ('fecha_devolucion', models.DateField(db_column='FECHA_DEVOLUCION')),
            ],
            options={
                'db_table': 'DEVOLUCION',
            },
        ),
        migrations.CreateModel(
            name='DevolucionMed',
            fields=[
                ('id_devolucion_det', models.IntegerField(db_column='ID_DEVOLUCION_DET', primary_key=True, serialize=False)),
                ('cantidad', models.FloatField(db_column='CANTIDAD')),
                ('precio_unitario', models.FloatField(db_column='PRECIO_UNITARIO')),
                ('total', models.FloatField(db_column='TOTAL')),
                ('id_devolucion', models.ForeignKey(blank=True, db_column='ID_DEVOLUCION', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Devolucion')),
            ],
            options={
                'db_table': 'DEVOLUCION_MED',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.IntegerField(db_column='ID_EMPRESA', primary_key=True, serialize=False)),
                ('nombre', models.TextField(db_column='NOMBRE')),
            ],
            options={
                'db_table': 'EMPRESA',
            },
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id_transaccion', models.IntegerField(db_column='ID_TRANSACCION', primary_key=True, serialize=False)),
                ('id_medic', models.IntegerField(db_column='ID_MEDIC')),
                ('cantidad', models.IntegerField(db_column='CANTIDAD')),
                ('precio_unitario', models.FloatField(db_column='PRECIO_UNITARIO')),
                ('total', models.FloatField(db_column='TOTAL')),
            ],
            options={
                'db_table': 'KARDEX',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id_lote', models.IntegerField(db_column='ID_LOTE', primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField(blank=True, db_column='FECHA_COMPRA', null=True)),
                ('cantidad', models.IntegerField(blank=True, db_column='CANTIDAD', null=True)),
                ('id_empresa', models.ForeignKey(blank=True, db_column='ID_EMPRESA', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Empresa')),
            ],
            options={
                'db_table': 'LOTE',
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamento', models.IntegerField(db_column='ID_MEDICAMENTO', primary_key=True, serialize=False)),
                ('nombre', models.TextField(db_column='NOMBRE')),
                ('precio', models.FloatField(db_column='PRECIO')),
            ],
            options={
                'db_table': 'MEDICAMENTO',
            },
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id_presentacion', models.IntegerField(db_column='ID_PRESENTACION', primary_key=True, serialize=False)),
                ('presentacion', models.TextField(db_column='PRESENTACION')),
            ],
            options={
                'db_table': 'PRESENTACION',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.IntegerField(db_column='ID_ROL', primary_key=True, serialize=False)),
                ('rol', models.TextField(db_column='ROL')),
            ],
            options={
                'db_table': 'ROL',
            },
        ),
        migrations.CreateModel(
            name='TipoMedicamento',
            fields=[
                ('id_tipo', models.IntegerField(db_column='ID_TIPO', primary_key=True, serialize=False)),
                ('tipo', models.TextField(db_column='TIPO')),
            ],
            options={
                'db_table': 'TIPO_MEDICAMENTO',
            },
        ),
        migrations.CreateModel(
            name='TipoOperacion',
            fields=[
                ('id_ope', models.IntegerField(db_column='ID_OPE', primary_key=True, serialize=False)),
                ('operacion', models.CharField(db_column='OPERACION', max_length=1)),
            ],
            options={
                'db_table': 'TIPO_OPERACION',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.IntegerField(db_column='ID_USER', primary_key=True, serialize=False)),
                ('nombre', models.TextField(db_column='NOMBRE')),
                ('apellido', models.TextField(db_column='APELLIDO')),
                ('id_empresa', models.ForeignKey(db_column='ID_EMPRESA', on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Empresa')),
                ('id_rol', models.ForeignKey(blank=True, db_column='ID_ROL', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Rol')),
            ],
            options={
                'db_table': 'USER',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.IntegerField(db_column='ID_VENTA', primary_key=True, serialize=False)),
                ('field_desc', models.IntegerField(db_column='_DESC')),
                ('fecha', models.DateField(db_column='FECHA')),
                ('total', models.FloatField(db_column='TOTAL')),
                ('id_user', models.ForeignKey(blank=True, db_column='ID_USER', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.User')),
            ],
            options={
                'db_table': 'VENTA',
            },
        ),
        migrations.CreateModel(
            name='VentaMed',
            fields=[
                ('id_venta_detalle', models.IntegerField(db_column='ID_VENTA_DETALLE', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, db_column='CANTIDAD', null=True)),
                ('precio_neto', models.FloatField(blank=True, db_column='PRECIO_NETO', null=True)),
                ('id_descuento', models.ForeignKey(blank=True, db_column='ID_DESCUENTO', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Descuento')),
                ('id_medicamento', models.ForeignKey(blank=True, db_column='ID_MEDICAMENTO', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Medicamento')),
                ('id_venta', models.ForeignKey(blank=True, db_column='ID_VENTA', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Venta')),
            ],
            options={
                'db_table': 'VENTA_MED',
            },
        ),
        migrations.AddField(
            model_name='medicamento',
            name='id_presentacion',
            field=models.ForeignKey(db_column='ID_PRESENTACION', on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Presentacion'),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='id_tipo',
            field=models.ForeignKey(db_column='ID_TIPO', on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.TipoMedicamento'),
        ),
        migrations.AddField(
            model_name='lote',
            name='id_medicamento',
            field=models.ForeignKey(blank=True, db_column='ID_MEDICAMENTO', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Medicamento'),
        ),
        migrations.AddField(
            model_name='kardex',
            name='id_ope',
            field=models.ForeignKey(db_column='ID_OPE', on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.TipoOperacion'),
        ),
        migrations.AddField(
            model_name='devolucion',
            name='id_venta',
            field=models.ForeignKey(blank=True, db_column='ID_VENTA', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Farmacia.Venta'),
        ),
    ]