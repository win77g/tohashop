# Generated by Django 2.2.11 on 2020-04-17 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20200406_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasketmodel',
            name='size',
        ),
    ]
