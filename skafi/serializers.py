from .models import *
from rest_framework import serializers


class SkafSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkafModel
        fields = ('id','name','podcateg','brend','image_1','image_2',
                  'slug','price','height','depth','width','description','description_short',
                  'discount','is_active','new_product','top','photoMenu','slider','comments')

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

class SkafImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkafImage
        fields = ('id','product','image','slug',)
