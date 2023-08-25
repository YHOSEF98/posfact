from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout

# Create your views here.
class IndexView(TemplateView):
    template_name = 'homepage/index.html'


class LoginFormView(LoginView):
    template_name = 'homepage/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categorias')
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'
        return context


class logoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    