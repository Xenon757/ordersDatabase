from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TestSerializer
from .models import test

# Create your views here.


class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = test.objects.all()
