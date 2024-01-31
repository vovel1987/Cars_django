from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Auto,Model,AutoImage
from .serializers import AutoSerializer,ModelSeriaizer,ImageSerializer

class AutosList(APIView):
    def get(self,request,format=None):
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return Response(serializer.data)
    
class ModelsList(APIView):
    def get(self,request,format=None):
        models = Model.objects.all()
        serializer= ModelSeriaizer(models,many=True)
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
        
     
        
      


          
      
