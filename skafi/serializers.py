from .models import *
from rest_framework import serializers


class SkafSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkafModel
        fields = ('id','name','podcateg','brend','image_1','image_2',
                  'slug','price_g450_st','price_g450_od','price_g600_st','price_g600_od','price_shelf_1','price_shelf_1','height','height_penal','depth','width','width_penal','description','description_short',
                  'discount','is_active','new_product','top','photoMenu','slider','comments')

class PodcategSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcateg
        fields = ('name','slug','meta_k','meta_d','description')

class HeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Height
        fields = ('name',)

class HeightPenalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Height_penal
        fields = ('name',)  

class WidhtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Width
        fields = ('name',)
        
class WidhtPenalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Width_penal
        fields = ('name',)        

class DepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depth
        fields = ('name',)

class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ('name','slug',)

class SkafImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkafImage
        fields = ('id','product','image','slug',)
