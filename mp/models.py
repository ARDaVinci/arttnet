from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Messageprive(models.Model):
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sender')
    receiver = models.ForeignKey(User , on_delete=models.CASCADE , related_name='receiver')
    creation_date = models.DateTimeField(auto_now=True , auto_now_add=False)
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=5000)
    all_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mp:message_details', kwargs={'pk':self.pk})

