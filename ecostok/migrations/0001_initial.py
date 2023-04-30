# Generated by Django 3.2.14 on 2023-04-29 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('cod', models.CharField(help_text='Código do Material', max_length=3, primary_key=True, serialize=False)),
                ('descricao', models.CharField(help_text='Descrição do Material em Estoque', max_length=50)),
                ('peso', models.DecimalField(decimal_places=2, help_text='Peso do Material em Estoque em Kg', max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Preco_compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cod', models.ForeignKey(help_text='Código Material que Será Comprado', on_delete=django.db.models.deletion.CASCADE, to='ecostok.material')),
            ],
        ),
    ]