# Generated by Django 4.1.4 on 2023-01-08 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_hospitalstaff_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outpatientreport',
            name='patient',
        ),
        migrations.DeleteModel(
            name='OutPatient',
        ),
        migrations.DeleteModel(
            name='OutPatientReport',
        ),
    ]
