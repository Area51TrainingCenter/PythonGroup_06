from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # render_template('index.html', **contexto)
        contexto = super(HomeView, self).get_context_data(**kwargs)
        contexto['nombre'] = 'moises'
        return contexto
