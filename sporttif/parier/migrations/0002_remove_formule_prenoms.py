# Generated by Django 2.2.3 on 2019-08-01 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parier', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formule',
            name='prenoms',
        ),
    ]
