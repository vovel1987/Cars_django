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
            'get_absolute_url',
            'title',
            'hersteller',
            'kilometerstand',
        )

class ModelSeriaizer(serializers.ModelSerializer):
    class Meta:
        model= Model
        fields=(
            'title',
            'id',
            'get_image',
            'get_fahrz',


        )

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoImage
        fields=(
            'auto',
            'image',
            'get_image',
            'title',
            'get_absolute_url',
            'slot',
            
        )

class BewertungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bewertung
        fields=(
            'auto',
            'autos_seite',
            'component_autos_seite',
            'element_in_component',
            'schaden_descr',
            'schaden_value',
            'preis',
            'get_image',
            'image_schaden',
            
        )

