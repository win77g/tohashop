from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from .serializers import *
from .pagination import PostPageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class SkafViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = SkafModel.objects.all()
    serializer_class = SkafSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filter_fields = ['slug','photoMenu','brend','new_product','height','depth','width']

    pagination_class = PostPageNumberPagination


class SkafHeightViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Height.objects.all()
    serializer_class = HeightSerializer
    # filter_fields = ('slug',)

class SkafDeepViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Depth.objects.all()
    serializer_class = DepthSerializer
    # filter_fields = ('slug',)

class SkafWidhtViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Width.objects.all()
    serializer_class = WidhtSerializer
    # filter_fields = ('slug',)

class SkafBrendViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer

class GetSkafImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = SkafImage.objects.all()
    serializer_class = SkafImageSerializer
    filter_fields = ('product',)
