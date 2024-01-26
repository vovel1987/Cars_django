from django.db import models

# Create your models here.
class Model(models.Model):
    title= models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Autos(models.Model):
    kennzeichen = models.CharField(max_length=150)
    name= models.CharField(max_length=200)
    vorname = models.CharField(max_length=250)
    date= models.CharField(max_length=200)
    vin= models.CharField()
    besitzer= models.CharField(max_length=250)
    modelId = models.ForeignKey()