# Generated by Django 4.1.4 on 2022-12-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_hiredpainting_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiredpainting',
            name='appl_rent',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
