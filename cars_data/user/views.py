from django.shortcuts import render
from django.http import Http404
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Auto,Model,AutoImage,Bewertung,AutoZubehor,AutoReifen,AutoLackMessung
from .serializers import AutoSerializer,ModelSeriaizer,ImageSerializer,BewertungSerializer,AutoZubehorSerializer,AutoReifenSerializer,AutoLackMessungSerializer

class AutosList(APIView):
    def get(self,request,format=None):
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return Response(serializer.data)
    
class ModelsList(generics.ListAPIView):
    queryset = Model.objects.all()

    def get(self,request,format=None):
        query = self.request.GET.get("search",'')
        print(query)
       
        
        models = Model.objects.all()
        if query !='undefined'  :
          
            models = Model.objects.filter(title__icontains=query)  
         
        
        if query=='':
            models = Model.objects.all()
              
        
           
        serializer= ModelSeriaizer(models,many=True)
        return Response(serializer.data)
    
class BewertungList(APIView):
   def get(self,request,format=None):
       bewertungs = Bewertung.objects.all()
       serializer= BewertungSerializer(bewertungs,many=True)
       return Response(serializer.data)

class BewertungAuto(APIView):
    def get_object(self,auto):
        try:
            return Bewertung.objects.filter(auto=auto)
        except Auto.DoesNotExist:
            raise Http404
        
    def get(self,request,auto,format=None):
       bewertungs = self.get_object(auto)
       serializer= BewertungSerializer(bewertungs,many=True)
       return Response(serializer.data)
    
class AutoZubehorList(APIView):
    def get_object(self,auto):
        try:
            return AutoZubehor.objects.filter(auto=auto)
        except:
            raise Http404
    def get(self,request,auto,format=None):
        zubehors = self.get_object(auto)
        serializer = AutoZubehorSerializer(zubehors,many=True)
        return Response(serializer.data)
        
class AutoReifenList(APIView):
    def get_object(self,auto):
        try:
            return AutoReifen.objects.filter(auto=auto)
        except:
            raise Http404
    
    def get(self,request,auto,format=None):
        reifens = self.get_object(auto)
        serializer = AutoReifenSerializer(reifens,many=True)
        return Response(serializer.data)


class AutoLackMessungList(APIView):
    def get_object(self,auto):
        try:
            return AutoLackMessung.objects.filter(auto=auto)
        except:
            return Http404
    def get(self,request,auto,format=None):
        mesungs = self.get_object(auto)
        serializer = AutoLackMessungSerializer(mesungs,many=True)
        return Response(serializer.data)


# class ImagesList(APIView):
#     def get(self,request,format=None):
#         images=AutoImage.objects.all()
#         serializer = ImageSerializer(images,many=True)
#         return Response(serializer.data)
    
class ImageList(APIView):
    # def get(self,request,format=None):
    #     autos = AutoImage.objects.all()
    #     serializer = ImageSerializer(autos, many=True)
    #     return Response(serializer.data)
     def get_object(self, model):
        try: 
            return AutoImage.objects.filter(auto=model).order_by("slot")
        except Auto.DoesNotExist:
            raise Http404
    
     def get(self, request, model, format=None):
        product = self.get_object(model)
        serializer = ImageSerializer(product,many=True)
        return Response(serializer.data)


class ModelAutos(APIView):

    def get_object(self, model_id):
        try: 
            return Auto.objects.filter(model=model_id)
        except Auto.DoesNotExist:
            raise Http404
    
    def get(self, request, model_id, format=None):
        product = self.get_object(model_id)
        serializer = AutoSerializer(product,many=True)
        return Response(serializer.data)
      

class ModelAuto(APIView):
     
     def get_auto(self,model_id):
        try:
            return  Auto.objects.filter(id=model_id)
        except Auto.DoesNotExist:
            raise Http404
        
     def get(self,request,model_id,format=None):
         auto = self.get_auto(model_id)
         serializer = AutoSerializer(auto,many=True)
         return Response(serializer.data) 
        
     
        
      


          
      
