from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from product.serializers import *
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .pagination import PostPageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from prihozhie.models import PrihozhieModel
from myagkayamebel.models import MyagkayamebelModel
from derevyannayamebel.models import DerevyannayamebelModel
from detskie.models import DetskieModel
from gostinye.models import GostinyeModel
from kuhni.models import KuhniModel
from skafi.models import SkafModel
from spalni.models import SpalniModel
from rest_framework.views import APIView
from rest_framework.response import Response
from itertools import chain
from django.db.models import Q
from skafi.pagination import PostPageNumberPagination
# вывод всех продуктов по категории
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filter_fields = ['categ','brend','tkan']

    pagination_class = PostPageNumberPagination#PageNumberPagination #LimitOffsetPagination

class GetCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('slug',)
# class Search(APIView):
#      permission_classes = [permissions.AllowAny, ]
#      def get(self, request, format):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer
#         filter_backends = [SearchFilter]
#         search_fields = ['categ','brend','tkan']
#         return Response(serializer.data)


class SearchAPIView(APIView):
      permission_classes = [permissions.AllowAny, ]
      serializer = ProductSerializer
      def post(self, request, format=None, *args, **kwargs):
          q = request.data['q']
          q = q.lower()
          q = q.capitalize()
          print(q)
          prihozhie = PrihozhieModel.objects.filter(
              Q(category__name=q) | Q(brend__name=q) | Q(name=q)
          )
          myagkayamebel = MyagkayamebelModel.objects.filter(
              Q(category__name=q) | Q(brend__name=q) | Q(name=q)
          )
          derevyannayamebel = DerevyannayamebelModel.objects.filter(
              Q(category__name=q) | Q(brend__name=q) | Q(name=q)
          )
          detskie = DetskieModel.objects.filter(
              Q(category__name=q) | Q(brend__name=q) | Q(name=q)
          )
          gostinye = GostinyeModel.objects.filter(
              Q(category__name=q) | Q(brend__name=q) | Q(name=q)
          )
          kuhni = KuhniModel.objects.filter(
              Q(category__name=q) | Q(brend__name=q) | Q(name=q)
          )
          skafi = SkafModel.objects.filter(
              Q(brend__name=q) | Q(name=q)
          )
          spalni = SpalniModel.objects.filter(
              Q(brend__name=q) | Q(name=q)
          )
          queryset = list(chain(spalni,skafi,kuhni,prihozhie,myagkayamebel,derevyannayamebel,detskie,gostinye,))

          serializer = ProductSerializer(queryset,many=True)

          return Response({'data':serializer.data})

class ProductItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('slug',)





class GetProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_fields = ('product',)

class GetProductForHomeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('tkan','new_product','top')
