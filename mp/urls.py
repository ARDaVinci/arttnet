from django.conf.urls import url
from . import views

app_name = 'mp'

urlpatterns = [
    url(r'^messages/$' , views.MessageList.as_view() , name= 'message_list'),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view(), name='message_details'),
    url(r'^messages/create/$', views.MessageCreate.as_view(), name='message_create'),

]
