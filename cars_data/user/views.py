from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Auto,Model
from .serializers import AutoSerializer,ModelSeriaizer

class AutosList(APIView):
    def get(self,request,format=None):
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return Response(serializer.data)
    
class ModelsList(APIView):
    def get(self,request,fromat=None):
        models = Model.objects.all()
        serializer= ModelSeriaizer(models,many=True)
        return Response(serializer.data)
