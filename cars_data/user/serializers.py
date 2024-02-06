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
            # 'get_thumbnail',
            # 'get_absolute_url',
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

class AutoZubehorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoZubehor
        fields =(
           
            'zweitschlüssel',
            'paletot',
            'rad_8_fach',
            'windschott',
            'FBAKS',
            'reifenfüllkit',
            'servicemappe',
            'elektronikkarte',
            'bordwerkzeug',
            'warndreieck',
            'radiokarte',
            'ladegerät',
            'verbandskasten',
            'garantieheft',
            'zusatzInfo',
            'bremse',

        )


class AutoReifenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoReifen
        fields=(
            'reifen',
            'reifenname',
            'profil',
            'dimension',
            'index',
            'dot',
            'tpms',
            'winter',
            'verschlies',
            'belage',
            'stange',
            'radspiel',
            'lenspiel',
        )


class AutoLackMessungSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoLackMessung
        fields=(
            'kotflügelFS',
            'türFS',
            'seitenpaneleFS',
            'schwellerFS',
            'kotflügelBS',
            'türBS',
            'seitenpaneleBS',
            'schwellerBS',
            'stosStangeF',
            'motorhaubeF',
            'heckHeck',
            'stosStangeHeck',
            'spoilerHeck',
            'dach',
            'hardTopDach',
        )

