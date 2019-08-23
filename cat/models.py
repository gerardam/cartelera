from django.db import models
from base.models import ClaseModelo


########## GENEROS ##########
class Genero(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del género',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def Save(self):
        self.descripcion = self.descripcion.upper()
        super(Genero, self).Save()

    class Meta:
        verbose_name_plural = 'Géneros'
    