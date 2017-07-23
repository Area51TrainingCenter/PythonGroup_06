from django.contrib import admin

from pedidos.models import Pedido, CantidadProducto


class CantidadProductoInline(admin.TabularInline):
    model = CantidadProducto
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha_creacion', 'usuario', 'estado', 'tipo_pago')
    list_display_links = list_display
    list_filter = ('fecha', 'estado', 'tipo_pago',)
    inlines = (CantidadProductoInline,)

    def fecha_creacion(self, instancia):
        return instancia.fecha.strftime('%d/%m/%Y %H:%S')


admin.site.register(Pedido, PedidoAdmin)
