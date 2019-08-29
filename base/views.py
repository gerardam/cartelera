from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,\
        PermissionRequiredMixin
from django.views import generic
from django.db.models import Q
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


class HomeSinAcceso(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/sinacceso.html'
    login_url = 'base:login'


def Home(request):
    queryset = request.GET.get('buscar')
    pelicula = Pelicula.objects.filter(edo = True).order_by('-id')[:36]
    genero = Genero.objects.filter(edo = True)
    if queryset:
        pelicula = Pelicula.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(director__icontains = queryset)
        ).distinct().order_by('-id')[:12]
    return render(request, 'base/home.html', {'obj':pelicula, 'gen':genero})
# class Home(generic.TemplateView):
    # template_name = 'base/home.html'
    # pelicula = Pelicula.objects.filter(edo=True)
    # context_object_name = 'obj'


def FilGenero(request, gen_id=None):
    queryset = request.GET.get('buscar')
    pelicula = Pelicula.objects.filter(genero=gen_id).order_by('-id')[:36]
    genero = Genero.objects.filter(edo = True)
    if queryset:
        pelicula = Pelicula.objects.filter(genero=gen_id).filter(
            Q(titulo__icontains = queryset) |
            Q(director__icontains = queryset)
        ).distinct().order_by('-id')[:12]
    return render(request, 'base/home.html', {'obj':pelicula, 'gen':genero})


def FichaPeli(request, pel_id=None):
    queryset = request.GET.get('buscar')
    pelicula = Pelicula.objects.filter(id = pel_id).first()
    genero = Genero.objects.filter(edo = True)
    if queryset:
        pelicula = Pelicula.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(director__icontains = queryset)
        ).distinct().order_by('-id')[:12]
        return render(request, 'base/home.html', {'obj':pelicula, 'gen':genero})
    else:
        return render(request, 'base/ficha.html', {'obj':pelicula, 'gen':genero})
