# Generated by Django 2.0.6 on 2018-06-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataartista',
            name='foto_header',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='fechas',
            name='cache_total',
            field=models.IntegerField(blank=True, help_text='Caché total a cobrar'),
        ),
        migrations.AlterField(
            model_name='fechas',
            name='gastos',
            field=models.IntegerField(blank=True, help_text='Gastos logísticos'),
        ),
    ]
