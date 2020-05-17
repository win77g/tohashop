from .models import *
from rest_framework import serializers


class WishlistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistModel
        fields = ('id','token_key','product_name','category'
                  ,'slug','price'
                  ,'image',
                  'brend',
                  'created')


