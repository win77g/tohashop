# Generated by Django 2.2.11 on 2020-04-27 17:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('derevyannayamebel', '0006_podcateg_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcateg',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=120, null=True, unique=True, verbose_name='Описание'),
        ),
    ]
