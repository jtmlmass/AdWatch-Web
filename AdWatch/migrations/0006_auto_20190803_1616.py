# Generated by Django 2.2.4 on 2019-08-03 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdWatch', '0005_auto_20190802_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='frecuencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdWatch.Frecuencia'),
        ),
    ]