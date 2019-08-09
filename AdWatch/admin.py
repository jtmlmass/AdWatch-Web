from .models import Frecuencia, FechaTrans, Anuncio, HorarioTrans, TipoAnuncio, Fingerprint, Registro
from django.contrib import admin
from django.contrib.auth.models import User

# Personalización de Página

# HorarioTrans


class HorarioTransInline(admin.TabularInline):
    model = HorarioTrans
    extra = 1

# FechaTrans


class FechaTransInline(admin.TabularInline):
    inlines = [HorarioTransInline]
    model = FechaTrans
    extra = 1


class TipoAnuncioAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'descripcion', 'creado', 'actualizado']
    list_per_page = 20
    list_filter = ['tipo', 'creado', 'actualizado']


class FrecuenciaAdmin(admin.ModelAdmin):
    list_display = ['direccion', 'creado', 'actualizado']
    list_per_page = 30
    list_filter = ['direccion', 'creado', 'actualizado']


class AnuncioAdmin(admin.ModelAdmin):
    inlines = [FechaTransInline]
    list_filter = ['titulo', 'frecuencia', 'cliente', 'tipo',
                   'creado', 'actualizado']
    list_per_page = 10
    list_display = ['titulo', 'cliente', 'frecuencia', 'tipo',
                    'tiempo', 'creado', 'actualizado']
    ordering = ['cliente', 'frecuencia', 'titulo']


class FechaTransAdmin(admin.ModelAdmin):
    inlines = [HorarioTransInline]
    list_display = ['fecha', 'anuncio', 'creado', 'actualizado']
    list_per_page = 30
    list_filter = ['fecha', 'anuncio', 'creado', 'actualizado']


class HorarioTransAdmin(admin.ModelAdmin):
    list_display = ['tiempo', 'fecha', 'creado', 'actualizado']
    list_per_page = 30
    list_filter = ['tiempo', 'fecha', 'creado', 'actualizado']


class FingerprintAdmin(admin.ModelAdmin):
    list_display = ['index', 'anuncio', 'creado', 'actualizado']
    list_per_page = 15
    list_filter = ['index', 'anuncio', 'creado', 'actualizado']


class RegistroAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'anuncio', 'tiempo',
                    'fecha', 'creado', 'actualizado']
    list_per_page = 30
    list_filter = ['fecha', 'anuncio', 'tiempo',
                   'fecha', 'creado', 'actualizado']


# Register your models here.
admin.site.register(Frecuencia, FrecuenciaAdmin)
admin.site.register(Fingerprint, FingerprintAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(FechaTrans, FechaTransAdmin)
admin.site.register(HorarioTrans, HorarioTransAdmin)
admin.site.register(TipoAnuncio, TipoAnuncioAdmin)
admin.site.register(Anuncio, AnuncioAdmin)
