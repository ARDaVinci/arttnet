from django.views.generic import ListView, DetailView, CreateView, UpdateView,  DeleteView
from .models import Circulaire
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.urls import reverse_lazy

class Tableau_de_circulaires(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'circulaires.view_circulaire'
    login_url = '/intranet_artt/login/'
    template_name = 'circulaires/list_de_circulaires.html'
    context_object_name = 'toutes_les_circulaires'
    def get_queryset(self):
        return Circulaire.objects.all()


class CircCreate(LoginRequiredMixin , PermissionRequiredMixin, CreateView):
    permission_required = ('circulaires.add_circulaire','circulaires.view_circulaire' )
    login_url = '/intranet_artt/login/'
    model = Circulaire
    fields = ['title' , 'file']

class CircUpdate(LoginRequiredMixin , PermissionRequiredMixin, UpdateView):
    permission_required = ('circulaires.change_circulaire','circulaires.view_circulaire' )
    login_url = '/intranet_artt/login/'
    model = Circulaire
    fields = ['title' , 'file']

class CircDelete(LoginRequiredMixin , PermissionRequiredMixin, DeleteView):
    permission_required = ('circulaires.change_circulaire','circulaires.view_circulaire' )
    login_url = '/intranet_artt/login/'
    model = Circulaire
    success_url = reverse_lazy('circulaires:circulaires')


