from django.urls import path, re_path
from .views import OrderPlaceView
from .views import OrderCommitView
from .views import OrderPayView
from .views import CheckPayView
from .views import CommentView

app_name = 'order'
urlpatterns = [
    re_path(r'^place$', OrderPlaceView.as_view(), name='place'),  # 提交订单
    re_path(r'^commit$', OrderCommitView.as_view(), name='commit'),  # 订单创建,
    re_path(r'^pay$', OrderPayView.as_view(), name='pay'),  # 订单支付,
    re_path(r'^check$', CheckPayView.as_view(), name='check'),  # 查询支付交易结果,
    re_path(r'^comment/(?P<order_id>\d+)$', CommentView.as_view(), name='comment')  # 订单评论,
]
