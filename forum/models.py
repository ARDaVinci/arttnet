from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Post(models.Model):
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name= 'post_sender' , null= True)
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=3000)
    total_comments = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now= True , auto_now_add=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:posts")

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete= models.CASCADE, related_name='comments')
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.TextField(max_length= 3000 )
    creation_date = models.DateTimeField(auto_now=True ,auto_now_add=False)
    comment_id = models.IntegerField(null=True)
    slug = models.SlugField( null=True)


    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('posts:post', kwargs= {'pk':post.pk})

    class Meta:
        ordering = [ '-comment_id']

