from rest_framework import serializers

from goods.models import Goods
from .models import ShoppingCart


class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(min_value=1, label='数量', required=True, error_messages={
        'min_value': '商品数量不能小于1',
        'required': '请选择购买数量',
    })
    goods = serializers.PrimaryKeyRelatedField(label='商品', required=True, queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context['request'].user
        nums = validated_data['nums']
        goods = validated_data['goods']
        existed = ShoppingCart.objects.filter(user=user, goods=goods)
        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        return existed
