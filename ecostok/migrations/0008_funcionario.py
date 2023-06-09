# Generated by Django 3.2.14 on 2023-04-30 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecostok', '0007_auto_20230429_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('cpf', models.CharField(help_text='CPF dos Funcionarios', max_length=11, primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Nome do Funcionario', max_length=50)),
                ('sobrenome', models.CharField(help_text='Sobrenome do Funcionario', max_length=50)),
                ('pagamento', models.ForeignKey(help_text='Id da Transação', on_delete=django.db.models.deletion.PROTECT, to='ecostok.caixa')),
            ],
        ),
    ]
