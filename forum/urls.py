from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^posts/$' , views.PostList.as_view() , name= 'posts'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post'),
    url(r'^posts/create/$', views.PostCreate.as_view(), name='create_post'),
    url(r'^posts/(?P<pk>[0-9]+)/update/$', views.PostUpdate.as_view(), name='update_post'),
    url(r'^posts/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='delete_post'),
    url(r'^posts/(?P<pk>[0-9]+)/comment/$', views.add_comment, name='comment'),
    url(r'^posts/(?P<pk>[0-9]+)/comment/(?P<slug>[0-9]+)/update/$', views.update_comment, name='update_comment'),
    url(r'^posts/(?P<pk>[0-9]+)/comment/(?P<slug>[0-9]+)/delete/$', views.delete_comment, name='delete_comment'),

]
