from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser 
# Create your models here.






class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='api/static/images/profiles/' , blank=True) # or whatever
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.user.username





class Post(models.Model):



    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    image = models.ImageField(upload_to='api/static/images/posts/' ,blank=True)
    body=models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    auth=models.ForeignKey(User,on_delete=models.PROTECT)


    class Meta:
        ordering = ['-publish']
        indexes = [
        models.Index(fields=['-publish']),
        ]


    def __str__(self) :
        return self.title
    

class PostComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) 
        
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        
        return f'Comment by {self.user} on {self.post}'
    


