from django.contrib import admin
from AdWatch.models import Frecuencia, FechaTrans, Anuncio, HorarioTrans, TipoAnuncio, Fingerprint, Registro

# Register your models here.


class HorarioTransInline(admin.TabularInline):
    model = HorarioTrans
    extra = 1


class FechaTransInline(admin.TabularInline):
    inlines = [HorarioTransInline]
    model = FechaTrans
    extra = 1


class AnuncioAdmin(admin.ModelAdmin):
    inlines = [FechaTransInline]
    list_filter = ['titulo', 'frecuencia', 'cliente', 'tipo']
    list_per_page = 10
    list_display = ['titulo', 'cliente', 'frecuencia', 'tipo',
                    'tiempo']
    ordering = ['cliente', 'frecuencia', 'titulo']


admin.site.register(Anuncio, AnuncioAdmin)
