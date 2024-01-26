from django.db import models

# Create your models here.
class Model(models.Model):
    title= models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Auto(models.Model):
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING, related_name="autos")


    kennzeichen = models.CharField(max_length=150)
    name = models.CharField(max_length=200)
    vorname = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField()
    vin = models.CharField(max_length=200)
    firma = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.kennzeichen
