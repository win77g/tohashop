# Generated by Django 2.2.11 on 2020-09-17 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prihozhie', '0003_auto_20200428_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True, unique=True, verbose_name='Высота')),
                ('slug', models.SlugField(blank=True, default=None, null=True, unique=True, verbose_name='Транслит')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серия',
            },
        ),
        migrations.AddField(
            model_name='prihozhiemodel',
            name='seria',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='prihozhie.Seria', to_field='slug', verbose_name='Серия'),
        ),
    ]
