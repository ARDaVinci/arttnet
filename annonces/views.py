from django.views.generic import ListView, DetailView, CreateView, UpdateView,  DeleteView
from .models import Annonce
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.urls import reverse_lazy

class Tableau_d_annonces(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'annonces.view_annonce'
    login_url = '/intranet_artt/login/'
    template_name = 'annonces/liste_d_annonces.html'
    context_object_name = 'toutes_les_annonces'
    def get_queryset(self):
        return Annonce.objects.all()


class AnnonceCreate(LoginRequiredMixin , PermissionRequiredMixin, CreateView):
    permission_required = ('annonces.add_annonce','annonces.view_annonce' )
    login_url = '/intranet_artt/login/'
    model = Annonce
    fields = ['title' , 'file']

class AnnonceUpdate(LoginRequiredMixin , PermissionRequiredMixin, UpdateView):
    permission_required = ('annonces.change_annonce','annonces.view_annonce' )
    login_url = '/intranet_artt/login/'
    model = Annonce
    fields = ['title' , 'file']

class AnnonceDelete(LoginRequiredMixin , PermissionRequiredMixin, DeleteView):
    permission_required = ('annonces.change_annonce','annonces.view_annonce' )
    login_url = '/intranet_artt/login/'
    model = Annonce
    success_url = reverse_lazy('annonces:annonces')


