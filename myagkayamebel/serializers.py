from .models import *
from rest_framework import serializers


class MyagkayamebelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyagkayamebelModel
        fields = ('id','name','keyword','category','podcateg','brend','image_1','image_2',
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

class DepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depth
        fields = ('name',)

class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ('name','slug',)

class MyagkayamebelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyagkayamebelImage
        fields = ('id','product','image','slug',)
