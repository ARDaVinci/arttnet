from django.db import models
from django.urls import reverse

class Circulaire(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to= 'pdf_circulaires/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('circulaires:circulaires')


