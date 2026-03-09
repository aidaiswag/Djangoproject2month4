from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name
    
class Professions(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    


class Celebrity(models.Model):
    name = models.CharField(max_length=250)
    biography = models.TextField(max_length=300, null=True)
    career = models.CharField(max_length=250)
    childhood = models.CharField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to="celebrity_image")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    professions = models.ManyToManyField(Professions)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

