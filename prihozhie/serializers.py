from .models import *
from rest_framework import serializers


class PrihozhieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrihozhieModel
        fields = ('id','name','keyword','category','podcateg','brend','seria','image_1','image_2',
                  'slug','price','height','depth','width','description','description_short',
                  'discount','is_active','new_product','top','photoMenu','slider','comments')

class PodcategSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcateg
        fields = ('name','slug','meta_k','meta_d','description')

class HeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Height
        fields = ('name',)
class WidhtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Width
        fields = ('name',)

class WidthTumbForShuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidthTumbForShues
        fields = ('name',)        

class DepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depth
        fields = ('name',)

class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ('name','slug',)

class PrihozhieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrihozhieImage
        fields = ('id','product','image','slug',)
