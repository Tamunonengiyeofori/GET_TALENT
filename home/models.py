from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recruit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/profile_pictures')
    resume = models.FileField(upload_to='uploads/recruit_resume')
    track = models.CharField(max_length=10000)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=10000)
    state = models.CharField(max_length=10000)
    country = models.CharField(max_length=10000)
    b_link = models.CharField(max_length=10000, null=True, blank=True)
    linkedin_link = models.CharField(max_length=10000, null=True, blank=True)
    instagram_link = models.CharField(max_length=10000, null=True, blank=True)
    twitter_link = models.CharField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.user
    
class Experience(models.Model):
    owner = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    employer = models.CharField(max_length=10000)
    position = models.CharField(max_length=10000)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.owner
    
    
class Contact(models.Model):
    owner = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10000)
    email = models.CharField(max_length=10000)
    address = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.owner
    

class Review(models.Model):
    owner = models.ForeignKey(Recruit, on_delete=models.CASCADE)
   

    