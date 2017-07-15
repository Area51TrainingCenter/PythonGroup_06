from django.contrib import admin
from productos.models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    list_display_links = ('nombre', 'precio')
    search_fields = ('nombre',)
    list_filter = ('fecha_creacion',)

admin.site.register(Producto, ProductoAdmin)
