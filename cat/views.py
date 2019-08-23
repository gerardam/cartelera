from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from .models import Genero
from .forms import GeneroForm
from base.views import SinAcceso


########## GENEROS ##########
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

    def FormValido(self, form):
        form.instance.uc = self.request.user
        return super().FormValido(form)

class GeneroEdit(SinAcceso, generic.UpdateView):
    permission_required = 'cat.change_genero'
    model = Genero
    template_name = 'gen/genfor.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('cat:gelist')

    def FormValido(self, form):
        form.instance.um = self.request.user.id
        return super().FormValido(form)

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
        genero.estado = False
        genero.save()
        return redirect('cat:gelist')

    return render(request, template_name, contexto)