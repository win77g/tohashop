# Generated by Django 2.2.11 on 2020-04-27 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('derevyannayamebel', '0009_auto_20200427_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='derevyannayamebelmodel',
            name='mtad',
        ),
        migrations.RemoveField(
            model_name='derevyannayamebelmodel',
            name='mtak',
        ),
    ]
