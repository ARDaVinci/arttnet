from django.conf.urls import url
from . import views as entry_views
from django.contrib.auth import views as auth_views

app_name = 'entry_accounts'

urlpatterns = [
    url(r'login/$' , auth_views.LoginView.as_view(template_name='entry_accounts/login.html'), name= 'login' ),
    url(r'logout/$' ,auth_views.LogoutView.as_view(), name='logout'),
    url(r'^$' , entry_views.HomePage.as_view(),  name='homepage'),
    url(r'^salut/$' , entry_views.SalutPage.as_view(), name= 'salut'),
]
