from django.db import models
from django.urls import reverse

class Annonce(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to= 'pdf_annonces/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('annonces:annonces')

