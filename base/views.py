from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,\
        PermissionRequiredMixin
from django.views import generic


class SinAcceso(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'base:login'
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url = 'base:sinacceso'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(generic.TemplateView):
    template_name = 'base/home.html'

class HomeSinAcceso(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/sinacceso.html'
    login_url = 'base:login'