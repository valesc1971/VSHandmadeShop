# Generated by Django 4.0.4 on 2022-04-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='rut',
            field=models.CharField(default=' ', max_length=15),
            preserve_default=False,
        ),
    ]
