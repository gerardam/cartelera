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


########## PELICULA ##########
class Pelicula(ClaseModelo):
    titulo = models.CharField(max_length=100,blank=False)
    sinopsis = models.TextField(max_length=250,blank=False)
    director = models.CharField(max_length=100,null=False,blank=True)
    fecha_estreno = models.DateField(null=True,blank=False)
    duracion = models.CharField(max_length=15,blank=False)
    #imagen = models.URLField(max_length = 1000, null = False, blank = False)
    imagen = models.ImageField(upload_to='album/')
    genero = models.ManyToManyField(Genero, blank = True)
    
    def __str__(self):
        return '{}'.format(self.titulo)

    def save(self):
        self.titulo = self.titulo.upper()
        #self.sinopsis = self.sinopsis.upper()
        #self.director = self.director.upper()
        #self.duracion = self.duracion.upper()
        super(Pelicula,self).save()

    class Meta:
        verbose_name_plural = "Peliculas"
