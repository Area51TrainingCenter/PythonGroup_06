from django.contrib import admin
from django.utils.html import format_html

from productos.models import Producto, Categoria, ImagenProducto


class ImagenInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1
    fields = ('imagen', 'previsualizacion',)
    readonly_fields = ('previsualizacion',)

    def previsualizacion(self, instancia):
        if not instancia.imagen:
            return '(vacío)'
        return format_html('<img src="{}" width="80">'.format(instancia.imagen.url))


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    list_display_links = ('nombre', 'precio')
    search_fields = ('nombre',)
    list_filter = ('fecha_creacion',)
    inlines = (ImagenInline,)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
