from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from .models import Genero, Pelicula
from .forms import GeneroForm, PeliculaForm
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