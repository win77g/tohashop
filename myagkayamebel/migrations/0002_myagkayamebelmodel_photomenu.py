# Generated by Django 2.2.11 on 2020-04-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myagkayamebel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myagkayamebelmodel',
            name='photoMenu',
            field=models.BooleanField(default=False, verbose_name='Фото в меню'),
        ),
    ]
