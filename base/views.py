from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,\
        PermissionRequiredMixin
from django.views import generic
from cat.models import Genero,Pelicula


class SinAcceso(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'base:login'
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url = 'base:sinacceso'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

def Home(request):
    pelicula = Pelicula.objects.filter(edo = True)
    return render(request, 'base/home.html', {'obj':pelicula})

# class Home(generic.TemplateView):
    # template_name = 'base/home.html'
    # pelicula = Pelicula.objects.filter(edo=True)
    # context_object_name = 'obj'


def FilGenero(request, gen_id=None):
    pelicula = Pelicula.objects.filter(genero=gen_id)
    return render(request, 'base/home.html', {'obj':pelicula})


class HomeSinAcceso(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/sinacceso.html'
    login_url = 'base:login'