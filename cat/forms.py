from django import forms
from .models import Genero, Pelicula


########## GENERO ##########
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['descripcion', 'edo']
        labels = {'descripcion':'Descripcion del genero', 'edo':'Estado'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


########## PELICULA ##########
class PeliculaForm(forms.ModelForm):
    fecha_estreno = forms.DateInput()
    
    class Meta:
        model=Pelicula
        fields=['titulo','sinopsis','director',
            'fecha_estreno','duracion','imagen',
            'genero','url_video','edo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_estreno'].widget.attrs['readonly'] = True
