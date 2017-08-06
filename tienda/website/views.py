from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from productos.models import Producto
from pedidos.models import Pedido, CantidadProducto


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # render_template('index.html', **contexto)
        contexto = super(HomeView, self).get_context_data(**kwargs)
        contexto['productos'] = Producto.objects.all().order_by('-fecha_creacion')[:4]
        return contexto


class BuscarView(TemplateView):
    template_name = 'buscar.html'

    def get_context_data(self, **kwargs):
        contexto = super(BuscarView, self).get_context_data(**kwargs)

        termino = self.request.GET.get('termino')
        if termino:
            contexto['resultados'] = Producto.objects.all().filter(nombre__icontains=termino)

        return contexto


class DetalleView(DetailView):
    template_name = 'detalle.html'
    model = Producto
    context_object_name = 'producto'


class AgregarCarritoView(View):
    def post(self, request, *args, **kwargs):
        id_producto = request.POST['producto']
        cantidad = request.POST['cantidad']

        carrito = request.session['carrito'].copy()
        carrito[id_producto] = cantidad
        request.session['carrito'] = carrito

        return redirect('detalle', pk=id_producto)


class CarritoView(ListView):
    template_name = 'carrito.html'
    context_object_name = 'carrito'

    def get_queryset(self):
        resultado = []
        self.total = 0
        for id, cantidad in self.request.session['carrito'].items():
            producto = Producto.objects.get(pk=id)
            cantidad = int(cantidad)
            subtotal = producto.precio * cantidad
            resultado.append([producto, cantidad, subtotal])
            self.total += subtotal
        return resultado

    def get_context_data(self, **kwargs):
        contexto = super(CarritoView, self).get_context_data(**kwargs)
        contexto['total'] = self.total
        return contexto


class OrdenarView(TemplateView):
    template_name = 'gracias.html'

    def post(self, request, *args, **kwargs):
        pedido = Pedido()
        pedido.usuario = request.user
        pedido.tipo_pago = request.POST['pago']
        pedido.save()

        for id, cantidad in request.session['carrito'].items():
            cantidad_producto = CantidadProducto()
            cantidad_producto.pedido = pedido
            cantidad_producto.producto = Producto.objects.get(pk=id)
            cantidad_producto.cantidad = cantidad
            cantidad_producto.save()

        request.session['carrito'] = {}

        return self.get(request, *args, **kwargs)
