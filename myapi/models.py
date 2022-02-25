from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    upload = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name
