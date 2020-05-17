from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from .serializers import *
from skafi.pagination import PostPageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class DerevyannayamebelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = DerevyannayamebelModel.objects.all()
    serializer_class = DerevyannayamebelSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filter_fields = ['slug','brend','top','photoMenu','podcateg','height','depth','width']

    pagination_class = PostPageNumberPagination

class DerevyannayamebelPodcategViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Podcateg.objects.all()
    serializer_class = PodcategSerializer
    filter_fields = ['slug']
