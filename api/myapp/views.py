from django.shortcuts import render
from rest_framework import generics, filters
from myapp.models import Food
from myapp.serializer import FoodSerializer

class FoodAPIView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []

    search_fields = ['name','price']
    filter_backends = (filters.SearchFilter, )
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

