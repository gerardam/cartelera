from django import forms
from .models import Genero


########## GENEROS ##########
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
