from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import *

class ItemModelViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()