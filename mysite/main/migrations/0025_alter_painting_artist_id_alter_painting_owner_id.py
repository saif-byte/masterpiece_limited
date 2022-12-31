# Generated by Django 4.1.4 on 2022-12-31 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_painting_submit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='artist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.artist'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.owner'),
        ),
    ]
