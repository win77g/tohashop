from .models import *
from rest_framework import serializers
from spalni.models import SpalniModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpalniModel
        fields = ('id','name','keyword','category','podcateg','brend','image_1','image_2',
                  'slug','price','height','depth','width','description','description_short',
                  'discount','is_active','new_product','top','photoMenu','slider','comments')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','parent','slug','description','mta_k','mta_d')
class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ('name','slug')
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id','product','image','slug')
