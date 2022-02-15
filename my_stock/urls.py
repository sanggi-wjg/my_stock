"""my_stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from stocks import viewsets as stock_viewset
from stocks import views as stock_view

from users import viewsets as user_viewset
from users import views as user_view

from home import views as home_view

router = routers.DefaultRouter()
router.register(r'users', user_viewset.UserViewSet)
router.register(r'users', user_viewset.UserDetailViewSet)
router.register(r'groups', user_viewset.GroupViewSet)
router.register(r'markets', stock_viewset.MarketViewSet)
router.register(r'sectors', stock_viewset.SectorViewSet)
router.register(r'industries', stock_viewset.IndustryViewSet)
router.register(r'stocks', stock_viewset.StockViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('v1/', include(router.urls)),

    path("", home_view.HomeView.as_view(), name = 'home'),

    path('users/', include('users.urls')),
    path('stocks/', include('stocks.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
