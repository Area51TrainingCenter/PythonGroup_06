from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from website.views import HomeView, BuscarView, DetalleView, AgregarCarritoView, CarritoView, OrdenarView
from usuarios.views import LoginView, LogoutView, RegistroView, PerfilView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^buscador$', BuscarView.as_view(), name='buscar'),
    url(r'^producto/(?P<pk>\d+)$', DetalleView.as_view(), name='detalle'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout'),
    url(r'^registro', RegistroView.as_view(), name='registro'),
    url(r'^perfil', PerfilView.as_view(), name='perfil'),

    url(r'^agregar-carrito', AgregarCarritoView.as_view(), name='agregar_carrito'),
    url(r'^carrito', CarritoView.as_view(), name='carrito'),
    url(r'^ordenar', OrdenarView.as_view(), name='ordenar'),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
