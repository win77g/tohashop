from django.shortcuts import render
from .models import *
from kuhni.models import KuhniModel
from skafi.models import SkafModel
from gostinye.models import GostinyeModel
from prihozhie.models import PrihozhieModel
from spalni.models import SpalniModel
from detskie.models import DetskieModel
from myagkayamebel.models import  *
from derevyannayamebel.models import DerevyannayamebelModel
from rest_framework import viewsets,permissions
from wishlist.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class WishlistViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = WishlistModel.objects.all()
    serializer_class = WishlistModelSerializer


def querySet_to_list(qs):
    """
    this will return python list<dict>
    """
    return [dict(q) for q in qs]

class WishlistPost(APIView):
       def post(self,request):
           pr = []
           print(request.data)
           slug = request.data.get("product_name")
           token_key = request.data.get("token_key")
           category = request.data.get("category")
           if (category == 'kuhni'):
            pr = KuhniModel.objects.filter(slug=slug).values()
           if (category=='shkaf'):
            pr = SkafModel.objects.filter(slug=slug).values()
            product = querySet_to_list(pr)
            product = product[0]
            wish = WishlistModel.objects.get_or_create(token_key = token_key,
                                         product_name = product["name"],
                                         category = category,
                                         slug = slug,
                                         price =  product["price_g450_st"],
                                         image = product["image_1"],
                                         brend = product["brend_id"])
            return Response({'status':201})                              
           if (category=='gostinye'):
            pr = GostinyeModel.objects.filter(slug=slug).values()
           if (category=='prihozhie'):
            pr = PrihozhieModel.objects.filter(slug=slug).values()
           if (category=='spalni'):
            pr = SpalniModel.objects.filter(slug=slug).values()
           if (category=='detskie'):
            pr = DetskieModel.objects.filter(slug=slug).values()
           if (category=='derevyannayamebel'):
            pr = DerevyannayamebelModel.objects.filter(slug=slug).values()
           if (category=='myagkayamebel'):
            pr = MyagkayamebelModel.objects.filter(slug=slug).values()
           product = querySet_to_list(pr)
           product = product[0]
           wish = WishlistModel.objects.get_or_create(token_key = token_key,
                                         product_name = product["name"],
                                         category = category,
                                         slug = slug,
                                         price =  product["price"],
                                         image = product["image_1"],
                                         brend = product["brend_id"])


           return Response({'status':201})

class DeleteWishlist(APIView):

       def post(self,request):
          print(request.data)
          slug = request.data.get("slug")
          token_key = request.data.get("token_key")
          wishlist = WishlistModel.objects.filter(token_key=token_key,slug=slug)
          wishlist.delete()
          wishlist = WishlistModel.objects.filter(token_key=token_key)
          serializer = WishlistModelSerializer(wishlist,many=True)
          return Response({'data':serializer.data})
