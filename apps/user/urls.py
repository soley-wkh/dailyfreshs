from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .views import RegisterView
from .views import ActiveView
from .views import LoginView
from .views import LogoutView
from .views import UserInfoView
from .views import UserOrderView
from .views import AddressView

app_name = 'user'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 注册
    re_path(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 用户激活
    path('login/', LoginView.as_view(), name='login'),  # 登录
    path('logout', LogoutView.as_view(), name='logout'),  # 退出

    # re_path(r'^$', login_required(UserInfoView.as_view()), name='user'),  # 用户中心信息页
    # re_path(r'^order$', login_required(UserOrderView.as_view()), name='order'),  # 用户中心订单页
    # re_path(r'^address$', login_required(AddressView.as_view()), name='address'),  # 用户中心地址页

    re_path(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心信息页
    re_path(r'^order/(?P<page>\d+)$', UserOrderView.as_view(), name='order'),  # 用户中心订单页
    re_path(r'^address$', AddressView.as_view(), name='address'),  # 用户中心地址页

]
