# Generated by Django 4.2.2 on 2023-08-15 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_rename_prod_pedido_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
    ]