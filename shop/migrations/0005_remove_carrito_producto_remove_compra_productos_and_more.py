# Generated by Django 4.2 on 2024-04-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_categoria_padre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='detallecompra',
            name='producto',
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(to='shop.producto'),
        ),
    ]
