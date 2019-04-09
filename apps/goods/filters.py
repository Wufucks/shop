from django.db.models import Q
from rest_framework import generics
import django_filters

from goods.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    price_min = django_filters.NumberFilter(field_name='shop_price', help_text="最低价格", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'is_hot', 'is_new']
