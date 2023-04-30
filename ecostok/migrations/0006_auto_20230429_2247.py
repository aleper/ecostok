# Generated by Django 3.2.14 on 2023-04-30 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecostok', '0005_rename_caixa_id_coletores_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coletores',
            name='pagamento',
            field=models.ForeignKey(help_text='Id da Transação', on_delete=django.db.models.deletion.PROTECT, to='ecostok.caixa'),
        ),
        migrations.AlterField(
            model_name='preco_compra',
            name='cod',
            field=models.ForeignKey(help_text='Código Material que Será Comprado', on_delete=django.db.models.deletion.PROTECT, to='ecostok.material'),
        ),
        migrations.AlterField(
            model_name='preco_venda',
            name='cod',
            field=models.ForeignKey(help_text='Código Material que Será Vendido', on_delete=django.db.models.deletion.PROTECT, to='ecostok.material'),
        ),
    ]
