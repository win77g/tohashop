# Generated by Django 2.2.11 on 2020-04-28 13:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myagkayamebel', '0002_myagkayamebelmodel_photomenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='myagkayamebelmodel',
            name='keyword',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='Ключи'),
        ),
        migrations.AddField(
            model_name='podcateg',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=120, null=True, unique=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='podcateg',
            name='meta_d',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=120, null=True, unique=True, verbose_name='Мета описание'),
        ),
        migrations.AddField(
            model_name='podcateg',
            name='meta_k',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='Ключевые слова'),
        ),
    ]
