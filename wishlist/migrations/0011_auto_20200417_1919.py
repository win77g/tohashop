# Generated by Django 2.2.11 on 2020-04-17 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0010_auto_20200413_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistmodel',
            old_name='price_1',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='wishlistmodel',
            name='price_2',
        ),
        migrations.RemoveField(
            model_name='wishlistmodel',
            name='price_3',
        ),
        migrations.RemoveField(
            model_name='wishlistmodel',
            name='price_4',
        ),
        migrations.RemoveField(
            model_name='wishlistmodel',
            name='tkan',
        ),
    ]
