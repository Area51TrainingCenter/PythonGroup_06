from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from website.views import HomeView, BuscarView, DetalleView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^buscador$', BuscarView.as_view(), name='buscar'),
    url(r'^producto/(?P<pk>\d+)$', DetalleView.as_view(), name='detalle'),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
