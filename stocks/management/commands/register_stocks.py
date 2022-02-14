import math

import FinanceDataReader as fdr
from django.core.management.base import BaseCommand
from pandas import Series

from stocks.models import Sector, Industry, Stock, Market
from stocks.validators import validate_allow_market_name


class Command(BaseCommand):
    help = 'Register stocks'
    market: 'Market' = None

    def add_arguments(self, parser):
        parser.add_argument('market_name', type = str, help = 'Market Name')

    def initialize(self, **options):
        market_name = options.get('market_name')
        validate_allow_market_name(market_name)

        self.market = Market.objects.register_if_not_exist(market_name = market_name)

    def handle(self, *args, **options):
        self.stdout.write(f"[START] {self.help}", style_func = self.style.SUCCESS, ending = '\n')
        self.initialize(**options)

        market_name = options.get('market_name')
        datasets = fdr.StockListing(market_name)

        for index, data in datasets.iterrows():
            if is_stock_series(data):
                sector = Sector.objects.register_if_not_exist(data['Sector'])
                industry = Industry.objects.register_if_not_exist(data['Industry'])

                stock = Stock.objects.register_if_not_exist(
                    Stock(market = self.market, sector = sector, industry = industry,
                          stock_code = data['Symbol'], stock_name = data['Name'])
                )
                self.stdout.write(f"{stock.stock_name} get or create", style_func = self.style.NOTICE, ending = '\n')
            else:
                self.stdout.write(f"{data['Name']} is not stock", style_func = self.style.WARNING, ending = '\n')

        self.stdout.write(f"[FINISH] {self.help}", style_func = self.style.SUCCESS, ending = '\n')


def is_stock_series(data: Series) -> bool:
    """
    콜, 풋, ETF 제외
    """
    if isinstance(data['Sector'], float) and isinstance(data['Industry'], float):
        if math.isnan(data['Sector']) and math.isnan(data['Industry']):
            return False

    return True
