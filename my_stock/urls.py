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

from users.viewsets import UserViewSet, UserDetailViewSet, GroupViewSet
from stocks.viewsets import MarketViewSet, SectorViewSet, IndustryViewSet, StockViewSet

from home import views as home_view
from stocks.views import IndustryStockListAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserDetailViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'markets', MarketViewSet, basename = 'market')
router.register(r'sectors', SectorViewSet, basename = 'sector')
router.register(r'industries', IndustryViewSet, basename = 'industry')
router.register(r'stocks', StockViewSet, basename = 'stock')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace = 'auth')),
    path('api/v1/', include(router.urls)),
    path('api/v1/industries/stocks', IndustryStockListAPIView.as_view()),

    path("", home_view.HomeView.as_view(), name = 'home'),
    path('users/', include('users.urls')),
    path('stocks/', include('stocks.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]
