from typing import Any

from django.core.exceptions import ValidationError
from django.db import models

from stocks.validators import validate_allow_market_name


class MarketQuerySet(models.QuerySet):

    def register_if_not_exist(self, market_name: str) -> 'Market':
        try:
            return Market.objects.get(market_name = market_name)
        except Market.DoesNotExist:
            return self.register(market_name)

    def register(self, market_name: str) -> 'Market':
        market = Market(market_name = market_name)
        try:
            market.full_clean()
        except ValidationError as e:
            raise e
        else:
            market.save()
            return market


class Market(models.Model):
    objects = MarketQuerySet.as_manager()

    class MarketNames(models.TextChoices):
        KOSPI: str = 'KOSPI'
        KOSDAQ: str = 'KOSDAQ'

    id = models.BigAutoField(primary_key = True)
    market_name = models.CharField(max_length = 50, unique = True, null = False, blank = False,
                                   validators = [validate_allow_market_name],
                                   choices = MarketNames.choices, verbose_name = 'Market 명')

    class Meta:
        db_table = 'markets'
        ordering = ('id',)
        default_permissions = ('add', 'view')

    def __str__(self):
        return f"<Market:{self.id}> {self.market_name}"


class SectorQuerySet(models.QuerySet):

    def register_if_not_exist(self, sector_name: str) -> 'Sector':
        try:
            return Sector.objects.get(sector_name = sector_name)
        except Sector.DoesNotExist:
            return self.register(sector_name)

    def register(self, sector_name: str) -> 'Sector':
        sector = Sector(sector_name = sector_name)
        try:
            sector.full_clean()
        except ValidationError as e:
            raise e
        else:
            sector.save()
            return sector


class Sector(models.Model):
    objects = SectorQuerySet.as_manager()

    id = models.BigAutoField(primary_key = True)
    sector_name = models.CharField(max_length = 250, unique = True, null = False, blank = False)

    class Meta:
        db_table = 'sectors'
        ordering = ('id',)
        indexes = (models.Index(fields = ['sector_name'], name = 'index_sectors_sector_name'),)
        default_permissions = ('add', 'view')

    def __str__(self):
        return f"<Sector:{self.id}> {self.sector_name}"


class IndustryQuerySet(models.QuerySet):

    def register_if_not_exist(self, industry_name: str) -> 'Industry':
        try:
            return Industry.objects.get(industry_name = industry_name)
        except Industry.DoesNotExist:
            return self.register(industry_name)

    def register(self, industry_name: str) -> 'Industry':
        industry = Industry(industry_name = industry_name)
        try:
            industry.full_clean()
        except ValidationError as e:
            raise e
        else:
            industry.save()
            return industry


class Industry(models.Model):
    objects = IndustryQuerySet.as_manager()

    id = models.BigAutoField(primary_key = True)
    industry_name = models.CharField(max_length = 250, unique = True, null = False, blank = False)

    class Meta:
        db_table = 'industries'
        ordering = ('id',)
        indexes = (models.Index(fields = ['industry_name'], name = 'index_industries_industry_name'),)
        default_permissions = ('add', 'view')

    def __str__(self):
        return f"<Industry:{self.id}> {self.industry_name}"


class StockQuerySet(models.QuerySet):

    def register_if_not_exist(self, stock: 'Stock') -> 'Stock':
        try:
            if not stock.stock_code:
                raise ValidationError("Stock's stock_code is empty")
            if not stock.stock_name:
                raise ValidationError("Stock's stock_name is empty")

            return Stock.objects.get(stock_name = stock.stock_name, stock_code = stock.stock_code)
        except Stock.DoesNotExist:
            return self.register(stock)

    def register(self, stock: 'Stock') -> 'Stock':
        try:
            stock.full_clean()
        except ValidationError as e:
            raise e
        else:
            stock.save()
            return stock


class StockKospiManger(models.Manager):
    def get_queryset(self):
        return super(StockKospiManger, self).get_queryset().filter(market__name = "KOSPI")


class Stock(models.Model):
    objects = StockQuerySet.as_manager()
    kospi_object = StockKospiManger()

    id = models.BigAutoField(primary_key = True)
    market = models.ForeignKey(Market, on_delete = models.PROTECT, null = False, related_name = 'market_stocks')
    sector = models.ForeignKey(Sector, on_delete = models.PROTECT, null = False, related_name = 'sector_stocks')
    industry = models.ForeignKey(Industry, on_delete = models.PROTECT, null = False, related_name = 'industry_stocks')

    stock_code = models.CharField(max_length = 20, unique = True, null = False, blank = False)
    stock_name = models.CharField(max_length = 100, unique = True, null = False, blank = False)

    class Meta:
        db_table = 'stocks'
        ordering = ('id',)
        indexes = (
            models.Index(fields = ['market'], name = 'index_stocks_market'),
            models.Index(fields = ['sector'], name = 'index_stocks_sector'),
            models.Index(fields = ['industry'], name = 'index_stocks_industry'),
            models.Index(fields = ['stock_code'], name = 'index_stocks_stock_code'),
            models.Index(fields = ['stock_name'], name = 'index_stocks_stock_name'),
        )
        unique_together = (('stock_code', 'stock_name'),)
        default_permissions = ('add', 'view', 'change', 'delete')

    def __str__(self):
        return f"<Stock:{self.id}> {self.stock_code} {self.stock_name}"

    @property
    def market_name(self):
        return self.market.market_name


class StockPrice(models.Model):
    id = models.BigAutoField(primary_key = True)
    stock = models.ForeignKey(Stock, on_delete = models.PROTECT, null = False)

    open_price = models.DecimalField(max_digits = 20, decimal_places = 4, blank = False, null = False)
    high_price = models.DecimalField(max_digits = 20, decimal_places = 4, blank = False, null = False)
    low_price = models.DecimalField(max_digits = 20, decimal_places = 4, blank = False, null = False)
    close_price = models.DecimalField(max_digits = 20, decimal_places = 4, blank = False, null = False)
    date = models.DateField(blank = False, null = False, db_column = 'date')

    class Meta:
        db_table = 'stock_prices'
        ordering = ('id',)
        indexes = (
            models.Index(fields = ['stock'], name = 'index_stock_prices_stock'),
        )
        default_permissions = ('add', 'view', 'change')


class Etf(models.Model):
    id = models.BigAutoField(primary_key = True)
    market = models.ForeignKey(Market, on_delete = models.PROTECT, null = False)

    etf_code = models.CharField(max_length = 20, unique = True, null = False, blank = False)
    etf_name = models.CharField(max_length = 100, unique = True, null = False, blank = False)

    class Meta:
        db_table = 'etfs'
        ordering = ('id',)
        indexes = (
            models.Index(fields = ['etf_code'], name = 'index_etfs_etf_code'),
            models.Index(fields = ['etf_name'], name = 'index_etfs_etf_name'),
        )
        default_permissions = ('add', 'view', 'change', 'delete')

    def __str__(self):
        return f"<Etf:{self.id}> {self.etf_code} {self.etf_name}"
