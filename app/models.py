from django.db import models

# Create your models here.
class Projet(models.Model):
    titre = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    