from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Genero
from .forms import GeneroForm


########## GENEROS ##########
class GeneroView(generic.ListView):
    model = Genero
    template_name = 'cat/genlis.html'
    context_object_name = 'obj'

class GeneroNew(generic.CreateView):
    model = Genero
    template_name = 'cat/genfor.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('cat:gelist')

    def FormValido(self, form):
        form.instance.uc = self.request.user
        return super().FormValido(form)

class GeneroEdit(generic.UpdateView):
    model = Genero
    template_name = 'cat/genfor.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('cat:gelist')

    def FormValido(self, form):
        form.instance.um = self.request.user.id
        return super().FormValido(form)

def GeneroInac(request, id):
    genero = Genero.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'cat/gendel.html'

    if not genero:
        return redirect('cat:gelist')

    if request.method=='GET':
        contexto = {'obj':genero}

    if request.method=='POST':
        genero.estado = False
        genero.save()
        return redirect('cat:gelist')

    return render(request, template_name, contexto)