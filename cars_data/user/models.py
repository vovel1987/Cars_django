from django.db import models
from django.db.models import Count
from io import BytesIO
from PIL import Image
from django.core.files import File 

# Create your models here.
class Model(models.Model):
    title= models.CharField(max_length=200)
    slug= models.SlugField(null=True)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    fahrz = models.IntegerField( null= True)
    

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return  self.image.url
        return ''
    def get_fahrz(self):
        # numers = Auto.objects.all().count()
        # numers = Model.objects.annotate(num_model = Count('autos'))
       
        return self.autos.all().count()
        


class Auto(models.Model):
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING, related_name="autos")
    title= models.CharField(max_length=200,null=True)
    kennzeichen = models.CharField(max_length=150 ,null=True)
    name = models.CharField(max_length=200)
    vorname = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField()
    vin = models.CharField(max_length=200)
    firma = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail = models.ImageField(upload_to='uploads/',blank=True,null=True)
    hersteller=models.CharField(max_length=200,null=True)
    kilometerstand = models.IntegerField(null= True)

    def __str__(self):
        return self.kennzeichen
    
    def get_absolute_url(self):
        return f'/{self.model.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return   self.image.url
        return ''
    
    def get_thumbnail(self):
           if self.thumbnail:
            return  self.thumbnail.url
           else:
               if self.image:
                   self.thumbnail = self.make_thumbnail(self.image)
                   self.save()

                   return   self.thumbnail.url
               else:
                   return ''
               
    def make_thumbnail(self,image, size=(300,200)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail = File(thumb_io,name=image.name)
        return thumbnail


class AutoImage(models.Model):
    image_id = models.ForeignKey(Auto,on_delete=models.DO_NOTHING,related_name='images')
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='1/',blank=True,null=True)
    
    
    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image:
            return   self.image.url
        return ''