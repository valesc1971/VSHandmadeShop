# Generated by Django 4.0.4 on 2022-04-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0002_usuario_edad_usuario_nombre_usuario_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
            preserve_default=False,
        ),
    ]
