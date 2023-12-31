# Generated by Django 4.2.2 on 2023-08-12 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_client_options'),
        ('productos', '0003_product_cantidad_product_costo_product_created_and_more'),
        ('ventas', '0002_egreso_mesa_productosegreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='cli',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.client'),
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(max_length=2)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.client')),
                ('mesa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.mesa')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.product')),
            ],
        ),
    ]
