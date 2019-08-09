from django.db import models
from django.contrib.auth.models import User
from django import forms
from gdstorage.storage import GoogleDriveStorage
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator

import datetime


# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Frecuencia(models.Model):
    direccion = models.DecimalField(
        max_digits=5, decimal_places=1, validators=[MinValueValidator(88.1), MaxValueValidator(107.9)], unique=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.direccion)


class TipoAnuncio(models.Model):
    tipo = models.CharField(max_length=32)
    descripcion = models.CharField(max_length=256)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo


class Anuncio(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    frecuencia = models.ForeignKey(
        Frecuencia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=128)
    tiempo = models.IntegerField()
    tipo = models.ForeignKey(
        TipoAnuncio, on_delete=models.CASCADE)
    audioAnuncio = models.FileField(
        upload_to='audios-adwatch', storage=gd_storage, null=True, verbose_name="Archivo de Audio", validators=[FileExtensionValidator(['wav'])])
    creado = models.DateTimeField(
        auto_now_add=True)
    actualizado = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.titulo


class FechaTrans(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.date.today)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Fecha de Transmisión")
        verbose_name_plural = ("Fechas de Transmisión")

    def __str__(self):
        return str(self.anuncio) + '-' + str(self.fecha)


class HorarioTrans(models.Model):
    fecha = models.ForeignKey(FechaTrans, on_delete=models.CASCADE)
    tiempo = models.TimeField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Hora de Transmisión")
        verbose_name_plural = ("Horas de Transmisión")

    def __str__(self):
        return str(self.fecha) + '-' + str(self.tiempo)


class Fingerprint(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    hashbinary = models.CharField(max_length=32)
    index = models.CharField(max_length=64)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.creado + ' ' + self.anuncio


class Registro(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    fingerprint = models.ForeignKey(Fingerprint, on_delete=models.CASCADE)
    tiempo = models.TimeField()
    fecha = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
