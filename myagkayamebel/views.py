from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from .serializers import *
from skafi.pagination import PostPageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class MyagkayamebelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = MyagkayamebelModel.objects.all()
    serializer_class = MyagkayamebelSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filter_fields = ['slug','brend','photoMenu','podcateg','height','depth','width','top']

    pagination_class = PostPageNumberPagination

class MyagkayamebelPodcategViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Podcateg.objects.all()
    serializer_class = PodcategSerializer
    filter_fields = ['slug']

class GetMyagkayamebelImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = MyagkayamebelImage.objects.all()
    serializer_class = MyagkayamebelImageSerializer
    filter_fields = ('product',)