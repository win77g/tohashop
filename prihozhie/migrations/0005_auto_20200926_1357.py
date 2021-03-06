# Generated by Django 2.2.11 on 2020-09-26 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prihozhie', '0004_auto_20200917_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='WidthTumbForShues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True, unique=True, verbose_name='Ширина тумбы для обуви')),
            ],
            options={
                'verbose_name': 'Ширина',
                'verbose_name_plural': 'Ширина',
            },
        ),
        migrations.AddField(
            model_name='prihozhiemodel',
            name='widthforshues',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='prihozhie.WidthTumbForShues', to_field='name', verbose_name='Ширина'),
        ),
    ]
