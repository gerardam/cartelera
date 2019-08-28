from django.urls import path
from django.contrib.auth import views as auth_views
from base.views import Home, HomeSinAcceso, FilGenero, FichaPeli

urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', Home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'), name='logout'),
    path('sinacceso/', HomeSinAcceso.as_view(), name='sinacceso'),
    path('genero/<int:gen_id>',FilGenero, name="gefiltro"),
    path('ficha/<int:pel_id>',FichaPeli, name="peficha"),
]
