from django.db import models

# Create your models here.

class Celebrity(models.Model):
    name = models.CharField(max_length=250)
    biography = models.TextField(max_length=300, null=True)
    career = models.CharField(max_length=250)
    childhood = models.CharField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to="celebrity_image")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name