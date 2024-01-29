from rest_framework import  serializers
from .models import *

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields=(
            'model',
            'id',
            'kennzeichen',
            'name',
            'vorname',
            'date',
            'vin',
            'firma',
            'get_image',
            'get_thumbnail',
            'get_absolute_url'
        )

class ModelSeriaizer(serializers.ModelSerializer):
    class Meta:
        model= Model
        fields=(
            'title',
            'id',
              'get_image',

        )

