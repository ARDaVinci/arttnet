from django.conf.urls import url
from . import views

app_name= 'circulaires'

urlpatterns = [
    url(r'^circulaires/$', views.Tableau_de_circulaires.as_view(), name='circulaires'),
    url(r'^circulaires/add/$', views.CircCreate.as_view(), name='add_circ'),
    url(r'^circulaires/(?P<pk>[0-9]+)/$', views.CircUpdate.as_view(), name='change_circ'),
    url(r'^circulaires/(?P<pk>[0-9]+)/delete/$', views.CircDelete.as_view(), name='delete_circ'),

]
