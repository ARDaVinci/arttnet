from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'entry_accounts/page_d_accueil.html'

class SalutPage(TemplateView):
    template_name = 'entry_accounts/salut.html'

