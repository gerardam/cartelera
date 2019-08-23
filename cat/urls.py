from django.urls import path
from .views import GeneroView, GeneroNew, GeneroEdit, GeneroInac

urlpatterns = [
    path('genero/', GeneroView.as_view(), name='gelist'),
    path('genero/new', GeneroNew.as_view(), name='genew'),
    path('genero/edit/<int:pk>', GeneroEdit.as_view(), name='geedit'),
    path('genero/del/<int:pk>', GeneroInac, name='gedel'),
]
