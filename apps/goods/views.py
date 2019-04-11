from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend

from goods.filters import GoodsFilter
from .serializers import *
from .models import *
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication


# Create your views here.

# 商品 分页 过滤 搜索
class GoodsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


# 商品分类列表数据
class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotSearchWordsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = HotSearchWords.objects.all().order_by('-index')
    serializer_class = HotSearchWordsSerializer
