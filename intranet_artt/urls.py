from django.contrib import admin
from django.conf.urls import url , include

urlpatterns = [
    url(r'^intranet_artt/', include('annonces.urls', namespace='annonces')),
    url(r'^intranet_artt/', include('mp.urls', namespace='mp')),
    url(r'^intranet_artt/', include('forum.urls', namespace='forum')),
    url(r'^intranet_artt/', include('circulaires.urls', namespace='circulaires')),
    url(r'^intranet_artt/', include('entry_accounts.urls', namespace='entry_accounts')),
    url(r'^admin/', admin.site.urls),
]

