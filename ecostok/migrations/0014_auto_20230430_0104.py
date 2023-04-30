# Generated by Django 3.2.14 on 2023-04-30 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecostok', '0013_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('peso', models.DecimalField(decimal_places=2, help_text='Peso do Material Comprado Kg', max_digits=3)),
                ('valor', models.DecimalField(decimal_places=2, help_text='Valor Pago ao Coletor', max_digits=6)),
                ('cliente', models.ForeignKey(help_text='CNPJ do Cliente', on_delete=django.db.models.deletion.PROTECT, to='ecostok.cliente')),
                ('material', models.ForeignKey(help_text='Código do Material', on_delete=django.db.models.deletion.PROTECT, to='ecostok.material')),
                ('vendedor', models.ForeignKey(help_text='CPF do Vendedor', on_delete=django.db.models.deletion.PROTECT, to='ecostok.funcionario')),
            ],
        ),
    ]
