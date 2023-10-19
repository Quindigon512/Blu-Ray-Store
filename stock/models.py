from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 2000)
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.name
