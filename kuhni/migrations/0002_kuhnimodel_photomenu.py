# Generated by Django 2.2.11 on 2020-04-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuhni', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kuhnimodel',
            name='photoMenu',
            field=models.BooleanField(default=False, verbose_name='Фото в меню'),
        ),
    ]
