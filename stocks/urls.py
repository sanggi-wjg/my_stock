from django.urls import path, include

from . import views

app_name = 'stocks'

urlpatterns = [
    path("", views.StockViews.as_view(), name = "index")
]
