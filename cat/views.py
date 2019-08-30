from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from .models import Genero, Serie, Pelicula
from .forms import GeneroForm, SerieForm, PeliculaForm
from base.views import SinAcceso


########## GENERO ##########
class GeneroView(SinAcceso, generic.ListView):
    permission_required = 'cat.view_genero'
    model = Genero
    template_name = 'gen/genlis.html'
    context_object_name = 'obj'

class GeneroNew(SinAcceso, generic.CreateView):
    permission_required = 'cat.add_genero'
    model = Genero
    template_name = 'gen/genfor.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('cat:gelist')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class GeneroEdit(SinAcceso, generic.UpdateView):
    permission_required = 'cat.change_genero'
    model = Genero
    template_name = 'gen/genfor.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('cat:gelist')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('cat.change_genero', login_url='base:sinacceso')
def GeneroInac(request, id):
    genero = Genero.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'gen/gendel.html'

    if not genero:
        return redirect('cat:gelist')

    if request.method=='GET':
        contexto = {'obj':genero}

    if request.method=='POST':
        genero.edo = False
        genero.save()
        return redirect('cat:gelist')

    return render(request, template_name, contexto)


########## SERIE ##########
class SerieView(SinAcceso, generic.ListView):
    permission_required = 'cat.view_serie'
    model = Serie
    template_name = 'ser/serlis.html'
    context_object_name = 'obj'

class SerieNew(SinAcceso, generic.CreateView):
    permission_required = 'cat.add_serie'
    model = Serie
    template_name = 'ser/serfor.html'
    context_object_name = 'obj'
    form_class = SerieForm
    success_url = reverse_lazy('cat:selist')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SerieEdit(SinAcceso, generic.UpdateView):
    permission_required = 'cat.change_serie'
    model = Serie
    template_name = 'ser/serfor.html'
    context_object_name = 'obj'
    form_class = SerieForm
    success_url = reverse_lazy('cat:selist')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('cat.change_serie', login_url='base:sinacceso')
def SerieInac(request, id):
    serie = Serie.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'ser/serdel.html'

    if not serie:
        return redirect('cat:selist')

    if request.method=='GET':
        contexto = {'obj':serie}

    if request.method=='POST':
        serie.edo = False
        serie.save()
        return redirect('cat:selist')

    return render(request, template_name, contexto)


########## PELICULA ##########
class PeliculaView(SinAcceso, generic.ListView):
    permission_required = 'cat.view_pelicula'
    model = Pelicula
    template_name = 'pel/pellis.html'
    context_object_name = 'obj'

class PeliculaNew(SinAcceso, generic.CreateView):
    permission_required = 'cat.add_pelicula'
    model = Pelicula
    template_name = 'pel/pelfor.html'
    context_object_name = 'obj'
    form_class = PeliculaForm
    success_url = reverse_lazy('cat:pelist')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PeliculaEdit(SinAcceso, generic.UpdateView):
    permission_required = 'cat.change_pelicula'
    model = Pelicula
    template_name = 'pel/pelfor.html'
    context_object_name = 'obj'
    form_class = PeliculaForm
    success_url = reverse_lazy('cat:pelist')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('cat.change_pelicula', login_url='base:sinacceso')
def PeliculaInac(request, id):
    pelicula = Pelicula.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'pel/peldel.html'

    if not pelicula:
        return redirect('cat:pelist')

    if request.method=='GET':
        contexto = {'obj':pelicula}

    if request.method=='POST':
        pelicula.edo = False
        pelicula.save()
        return redirect('cat:pelist')

    return render(request, template_name, contexto)