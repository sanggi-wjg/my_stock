from rest_framework import serializers

from stocks.models import Stock, Market, Sector, Industry


class MarketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Market
        fields = ['market_name', 'url']


class SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sector
        fields = ['sector_name', 'url']


class IndustrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Industry
        fields = ['industry_name', 'url']


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ['market', 'sector', 'industry', 'stock_code', 'stock_name', 'url']
