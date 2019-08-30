from django.urls import path
from .views import GeneroView, GeneroNew, GeneroEdit, GeneroInac, \
    PeliculaView, PeliculaNew, PeliculaEdit, PeliculaInac, \
    SerieView, SerieNew, SerieEdit, SerieInac

urlpatterns = [
    path('genero/', GeneroView.as_view(), name='gelist'),
    path('genero/new', GeneroNew.as_view(), name='genew'),
    path('genero/edit/<int:pk>', GeneroEdit.as_view(), name='geedit'),
    path('genero/del/<int:id>', GeneroInac, name='gedel'),

    path('pelicula/', PeliculaView.as_view(), name='pelist'),
    path('pelicula/new', PeliculaNew.as_view(), name='penew'),
    path('pelicula/edit/<int:pk>', PeliculaEdit.as_view(), name='peedit'),
    path('pelicula/del/<int:id>', PeliculaInac, name='pedel'),

    path('serie/', SerieView.as_view(), name='selist'),
    path('serie/new', SerieNew.as_view(), name='senew'),
    path('serie/edit/<int:pk>', SerieEdit.as_view(), name='seedit'),
    path('serie/del/<int:id>', SerieInac, name='sedel'),
]
