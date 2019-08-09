# Generated by Django 2.2.4 on 2019-08-02 17:19

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('AdWatch', '0002_auto_20190802_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='audioAnuncio',
            field=models.FileField(null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='audios-adwatch'),
        ),
    ]