# Generated by Django 2.2.11 on 2020-04-28 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('derevyannayamebel', '0011_derevyannayamebelmodel_keyword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podcateg',
            old_name='mta_d',
            new_name='meta_d',
        ),
        migrations.RenameField(
            model_name='podcateg',
            old_name='mta_k',
            new_name='meta_k',
        ),
    ]
