# Generated by Django 4.0.4 on 2022-05-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0029_producto_stock_alter_producto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]