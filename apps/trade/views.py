from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
# 购物车人
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import ShopCartSerializer
from .serializers import ShoppingCart
from utils.permission import IsOwnerOrReadOnly


class ShopCartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = ShopCartSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = ShoppingCart.objects.all()
