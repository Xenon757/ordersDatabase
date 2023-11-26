from django.shortcuts import render
from rest_framework import viewsets
from .serializers import accountSerializer, orderSerializer
from .models import account, order

# Create your views here.


class accountView(viewsets.ModelViewSet):
    serializer_class = accountSerializer
    queryset = account.objects.all()


class orderView(viewsets.ModelViewSet):
    serializer_class = orderSerializer
    queryset = order.objects.all()
