from django.contrib.auth import views as auth_views, login
from django.shortcuts import redirect
from django.views.generic import FormView, UpdateView

from usuarios.forms import RegistroForm, PerfilForm
from usuarios.models import Perfil


class LoginView(auth_views.LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        if 'carrito' not in self.request.session:
            self.request.session['carrito'] = {}
        return super(LoginView, self).form_valid(form)


# class LogoutView(auth_views.LogoutView):
#     pass

LogoutView = auth_views.LogoutView


class RegistroView(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm

    def form_valid(self, form):
        usuario = form.save()
        perfil = Perfil()
        perfil.usuario = usuario
        perfil.direccion = form.cleaned_data.get('direccion')
        perfil.telefono = form.cleaned_data.get('telefono')
        perfil.edad = form.cleaned_data.get('edad')
        perfil.save()

        login(self.request, usuario, 'django.contrib.auth.backends.ModelBackend')

        return redirect('home')


class PerfilView(UpdateView):
    template_name = 'perfil.html'
    model = Perfil
    form_class = PerfilForm
    success_url = '/perfil'

    def get_object(self, queryset=None):
        return self.request.user.perfil
