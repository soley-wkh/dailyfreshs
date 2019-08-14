from django.urls import path, re_path
from .views import IndexView, DetailView, ListView

app_name = 'goods'
urlpatterns = [
    re_path(r'^index$', IndexView.as_view(), name='index'),  # 首页
    re_path(r'^goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'),  # 商品详情页
    re_path(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'),  # 商品列表页
]
