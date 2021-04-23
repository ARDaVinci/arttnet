from django.db import models
from django.contrib.auth import models as user_models



class Enseignant(models.Model):
    user = models.OneToOneField(user_models.User , on_delete= models.CASCADE)
    name = models.CharField(max_length=300 , default= 'e')
    classe = models.CharField(max_length= 30)
    discipline = models.CharField(max_length= 300)
    degree = models.CharField(max_length=5)
    is_a_man = models.BooleanField(default=True)
    new = models.BooleanField(default= False)

    def __str__(self):
        return self.name


class Educateurs(models.Model):
    user = models.OneToOneField(user_models.User, on_delete=models.CASCADE)
    name= models.CharField(max_length=300 , default= 'e')
    classe = models.CharField(max_length=30)
    is_a_man = models.BooleanField(default=True)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Direction(models.Model):
    user = models.OneToOneField(user_models.User , on_delete= models.CASCADE)
    name = models.CharField(max_length=300 , default= 'e')
    directeur = models.BooleanField()
    is_a_man = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Eleves(models.Model):
    user = models.OneToOneField(user_models.User , on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    classe = models.CharField(max_length= 300)
    is_a_boy = models.BooleanField()

    def __str__(self):
        return self.name

