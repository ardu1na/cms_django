from django.contrib import admin

from digesto.models import ItemDigesto, Tema, Archivo



class ItemDigestoAdmin(admin.ModelAdmin):
    list_display = ['publicado','numero', 'titulo', 'categoria', 'fecha',   'estado', 'alcance']
    search_fields = ['titulo','numero', 'resumen', 'texto']
    list_filter = ['categoria', 'estado', 'alcance']
    list_display_links = ['numero', 'titulo', 'categoria', 'fecha']
    list_editable = ['publicado',]
admin.site.register(ItemDigesto, ItemDigestoAdmin)

admin.site.register(Tema)
admin.site.register(Archivo)