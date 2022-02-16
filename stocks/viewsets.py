from rest_framework import viewsets, permissions

from stocks.models import (
    Stock, Market, Sector, Industry
)
from stocks.serializers import (
    StockSerializer, MarketSerializer, SectorSerializer, IndustrySerializer
)


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
