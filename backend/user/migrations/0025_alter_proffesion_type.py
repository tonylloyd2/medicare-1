# Generated by Django 4.1.4 on 2023-01-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_rename_area_proffesion_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proffesion',
            name='type',
            field=models.CharField(max_length=25),
        ),
    ]
