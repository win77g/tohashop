from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from .serializers import *
from skafi.pagination import PostPageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class SpalniViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = SpalniModel.objects.all()
    serializer_class = SpalniSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filter_fields = ['slug','brend','podcateg','photoMenu','height','depth','width','top']

    pagination_class = PostPageNumberPagination

class SpalniPodcategViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Podcateg.objects.all()
    serializer_class = PodcategSerializer
    filter_fields = ['slug']

    
class GetSpalniImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = SpalniImage.objects.all()
    serializer_class = SpalniImageSerializer
    filter_fields = ('product',)