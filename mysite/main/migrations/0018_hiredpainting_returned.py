# Generated by Django 4.1.4 on 2022-12-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_painting_hired'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiredpainting',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]