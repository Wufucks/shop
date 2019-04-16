"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
# from django.views.generic import TemplateView

import xadmin
from goods.views import HotSearchWordsViewSet, BannerViewSet, GoodsViewSet, CategoryViewSet,IndexCategoryViewSet
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from trade.views import ShopCartViewSet, OrderInfoViewSet,AlipayView
from shop.settings import MEDIA_ROOT
from user.views import SmsCodeViewSet, UserViewSet

from user_opertion.views import UserViewFavSet, LeavingMessageViewSet, AddressViewSet

router = DefaultRouter()
# 商品
router.register(r'goods', GoodsViewSet, base_name='goods')
# 商品分类
router.register(r'category', CategoryViewSet, base_name='category')
router.register(r'hotsearch', HotSearchWordsViewSet, base_name='hotsearch')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'banner',BannerViewSet,base_name='banner')
# 短信
router.register(r'codes', SmsCodeViewSet, base_name='codes')
router.register(r'userfavs', UserViewFavSet, base_name='userfavs')
router.register(r'leaving', LeavingMessageViewSet, base_name='leaving')
router.register(r'address', AddressViewSet, base_name='address')
router.register(r'shopcart', ShopCartViewSet, base_name='shopcart')
router.register(r'orders', OrderInfoViewSet, base_name='orders')
router.register(r'indexgoods',IndexCategoryViewSet,base_name='indexgoods')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'docs/', include_docs_urls(title='超市')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'index/',TemplateView.as_view(template_name='index.html'),name='index'),
    #     商品
    url(r'^', include(router.urls)),
    # url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),

]
