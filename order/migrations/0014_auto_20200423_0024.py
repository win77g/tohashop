# Generated by Django 2.2.11 on 2020-04-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20200418_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinordermodel',
            name='product',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Продукт'),
        ),
    ]
