# Generated by Django 4.1.3 on 2022-11-30 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='produtos',
        ),
        migrations.RemoveField(
            model_name='person',
            name='doc',
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Venda',
        ),
    ]
