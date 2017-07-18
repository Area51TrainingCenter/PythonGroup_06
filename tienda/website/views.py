from django.views.generic import TemplateView, DetailView
from productos.models import Producto


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
