from django.conf.urls import url
from . import views

app_name= 'annonces'

urlpatterns = [
    url(r'^annonces/$', views.Tableau_d_annonces.as_view(), name='annonces'),
    url(r'^annonces/add/$', views.AnnonceCreate.as_view(), name='add_annonce'),
    url(r'^annonces/(?P<pk>[0-9]+)/$', views.AnnonceUpdate.as_view(), name='change_annonce'),
    url(r'^annonces/(?P<pk>[0-9]+)/delete/$', views.AnnonceDelete.as_view(), name='delete_annonce'),

]
