# Generated by Django 2.2.11 on 2020-10-05 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skafi', '0003_auto_20201005_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skafmodel',
            name='depth',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='skafi.Depth', to_field='name', verbose_name='Глубина шкафа'),
        ),
        migrations.AlterField(
            model_name='skafmodel',
            name='height',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='skafi.Height', to_field='name', verbose_name='Высота шкафа'),
        ),
        migrations.AlterField(
            model_name='skafmodel',
            name='width',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='skafi.Width', to_field='name', verbose_name='Ширина шкафа'),
        ),
    ]
