from django.shortcuts import render
from django.http import HttpRequest

from django.views import View
from rest_framework import status, pagination, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

from stocks.models import Industry
from stocks.serializers import IndustryStockSerializer

from stocks.models import (
    Stock, Market, Sector, Industry
)
from stocks.serializers import (
    StockSerializer, MarketSerializer, SectorSerializer, IndustrySerializer
)


class StockViews(View):
    template_name = 'stock/stock_index.html'
    page_title = 'Stock'

    def get(self, request: HttpRequest):
        return render(request, self.template_name, {
            'page_title': self.page_title,
        })


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]


class SectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndustryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [permissions.IsAuthenticated]


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.prefetch_related('market', 'sector', 'industry').all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndustryStockListAPIView(generics.ListAPIView):
    queryset = Industry.objects.prefetch_related('industry_stocks').all()
    serializer_class = IndustryStockSerializer
    pagination_class = pagination.PageNumberPagination


class IndustryStockDetailAPIView(generics.RetrieveAPIView):
    queryset = Industry.objects.prefetch_related('industry_stocks').all()
    serializer_class = IndustryStockSerializer
