# Generated by Django 4.0.4 on 2022-05-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0027_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ciudad',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
