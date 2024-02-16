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
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return  self.image.url
        return ''
    def get_fahrz(self):
        return self.autos.all().count()
    def get_reparatur(self):
           result= self.autos.all().filter(bewertungs__schaden = True)
           if result:
               return True
         
           return False
    def get_preis(self):
        preis = self.autos.all().filter(bewertungs__preis__gt = 0)
        if preis:
            return True
        return False

        
        
 
        


class Auto(models.Model):
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING, related_name="autos")
    title= models.CharField(max_length=200,null=True)
    kennzeichen = models.CharField(max_length=150 ,null=True)
    name = models.CharField(max_length=200)
    vorname = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    vin = models.CharField(max_length=200)
    firma = models.CharField(max_length=250, null=True, blank=True)
    # slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    # thumbnail = models.ImageField(upload_to='uploads/',blank=True,null=True)
    hersteller=models.CharField(max_length=200,null=True)
    kilometerstand = models.IntegerField(null= True)
    # schaden=models.BooleanField(null= True)
  

    def __str__(self):
        return self.kennzeichen
    
    # def get_absolute_url(self):
    #     return f'/{self.model.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return   self.image.url
        return ''
    

    def get_reparatur(self):
       
           result=self.bewertungs.all().filter(schaden=True).distinct()
           if result:
               return True
         
           return False
    def get_preis(self):
        preis = self.bewertungs.all().filter(preis__gt = 0)
        if preis:
            return True
        return False
    
    # def get_thumbnail(self):
    #        if self.thumbnail:
    #         return  self.thumbnail.url
    #        else:
    #            if self.image:
    #                self.thumbnail = self.make_thumbnail(self.image)
    #                self.save()

    #                return   self.thumbnail.url
    #            else:
    #                return ''
               
    # def make_thumbnail(self,image, size=(300,200)):
    #     img=Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)
    #     thumb_io=BytesIO()
    #     img.save(thumb_io,'JPEG',quality=85)
    #     thumbnail = File(thumb_io,name=image.name)
    #     return thumbnail


def user_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
       return 'autos/auto_{0}/{1}'.format(instance.auto.id, filename)


class AutoImage(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.DO_NOTHING, related_name="images")
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to=user_directory_path,blank=True,null=True)

    # slug = models.SlugField(null=True)
    slot = models.PositiveSmallIntegerField(default=1)
    
    

    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image:
            return   self.image.url
    # def get_absolute_url(self):
    #     return f'/{self.auto.slug}/{self.slug}/'
   
    
def schaden_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
       return 'schaden/auto_{0}/{1}'.format(instance.auto.id, filename)
    
class Bewertung(models.Model):
    auto = models.ForeignKey(Auto,on_delete =models.DO_NOTHING,related_name='bewertungs')
   
    title = models.CharField(max_length= 250, null=True)
    autos_seite = models.CharField(max_length = 250)
    component_autos_seite = models.CharField(max_length=250)
    element_in_component = models.CharField(max_length=250,null=True, blank=True)
    schaden_descr = models.CharField(max_length=250)
    schaden_value= models.CharField(max_length = 250)
    preis = models.IntegerField(null=True, blank=True)
    image_schaden = models.ImageField(upload_to=schaden_directory_path,blank=True,null=True)
    schaden = models.BooleanField(null= True)
    zusatzReparatur = models.TextField(max_length=400,null=True,blank=True)
    serviceLeistung=models.IntegerField(null=True,blank=True)
    behoben=models.BooleanField(null=True,blank=True)
    wird_behoben=models.BooleanField(null=True,blank=True)



    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image_schaden:
            return self.image_schaden.url
        

class AutoZubehor(models.Model):
    auto = models.ForeignKey(Auto,on_delete=models.DO_NOTHING,related_name='zubehors')
    title = models.CharField(max_length = 200)
    zweitschlüssel = models.BooleanField()
    paletot = models.BooleanField()
    rad_8_fach= models.BooleanField()
    windschott = models.BooleanField()
    FBAKS = models.BooleanField()
    reifenfüllkit = models.BooleanField()
    servicemappe = models.BooleanField()
    elektronikkarte = models.BooleanField()
    bordwerkzeug = models.BooleanField()
    warndreieck = models.BooleanField()
    radiokarte = models.BooleanField()
    ladegerät = models.BooleanField()
    verbandskasten = models.BooleanField()
    garantieheft = models.BooleanField()
    zusatzInfo = models.CharField(max_length=250,null=True,blank=True)
    bremse = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.title
    
class AutoReifen(models.Model):
    auto = models.ForeignKey(Auto,on_delete=models.DO_NOTHING,related_name='reifens')
    title = models.CharField(max_length = 200)
    reifen = models.CharField(max_length=20)
    reifenname = models.CharField(max_length = 200)
    profil = models.CharField(max_length=100)
    dimension = models.CharField(max_length = 100)
    index = models.CharField(max_length=100)
    dot= models.CharField(max_length=100)
    tpms= models.CharField(max_length=100)
    winter= models.CharField(max_length=100)
    verschlies = models.CharField(max_length =100,null=True)
    belage = models.CharField(max_length=100 ,null=True)
    radspiel = models.CharField(max_length=100 ,null=True)
    lenspiel = models.CharField(max_length=100 ,null=True)
    stange = models.CharField(max_length=100 ,null=True)
    

    def __str__(self):
        return self.title
    
class AutoLackMessung(models.Model):
    auto = models.ForeignKey(Auto,on_delete=models.DO_NOTHING,related_name='messungs')
    title=models.CharField(max_length=50)
    kotflügelFS=models.CharField(max_length=50,null=True,blank=True)
    türFS=models.CharField(max_length=50,null=True,blank=True)
    seitenpaneleFS=models.CharField(max_length=50,null=True,blank=True)
    schwellerFS=models.CharField(max_length=50,null=True,blank=True)
    kotflügelBS=models.CharField(max_length=50,null=True,blank=True)
    türBS=models.CharField(max_length=50,null=True,blank=True)
    seitenpaneleBS=models.CharField(max_length=50,null=True,blank=True)
    schwellerBS=models.CharField(max_length=50,null=True,blank=True)
    stosStangeF= models.CharField(max_length=50,null=True,blank=True)
    motorhaubeF=models.CharField(max_length=50,null=True,blank=True)
    heckHeck=models.CharField(max_length=50,null=True,blank=True)
    stosStangeHeck=models.CharField(max_length=50,null=True,blank=True)
    spoilerHeck=models.CharField(max_length=50,null=True,blank=True)
    dach=models.CharField(max_length=50,null=True,blank=True)
    hardTopDach=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.title



    

    
















