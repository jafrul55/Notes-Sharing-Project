from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    audio_file = models.FileField(upload_to='audio/',null=True,blank=True)
    video_file = models.FileField(upload_to='video/',null=True,blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    shared_with = models.ManyToManyField(User,related_name='shared_notes',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

