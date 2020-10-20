# Generated by Django 2.2.11 on 2020-10-16 01:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skafi', '0005_auto_20201006_1750'),
    ]

    operations = [
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