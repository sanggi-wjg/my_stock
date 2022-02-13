import math

import FinanceDataReader as fdr
from django.core.management.base import BaseCommand
from pandas import Series

from my_stock.constants import ALLOW_MARKETS


class Command(BaseCommand):
    help = 'Register stocks'

    def add_arguments(self, parser):
        parser.add_argument('market_name', type = str, help = 'Market Name')

    def check_args(self, **options):
        market_name = options.get('market_name')
        if market_name not in ALLOW_MARKETS:
            raise Exception(f"{market_name} is not allowed")

    def handle(self, *args, **options):
        self.stdout.write(f"[START] {self.help}", style_func = self.style.SUCCESS, ending = '\n')
        self.check_args(**options)

        market_name = options.get('market_name')
        datasets = fdr.StockListing(market_name)
        print(datasets.head(20))

        cnt = 0
        for index, data in datasets.iterrows():
            if cnt == 1000:
                break
            # print(index, data)
            print(f"{data['Symbol']}\t {data['Market']}\t {data['Name']}\t {data['Sector']}{type(data['Sector'])}\t {data['Industry']}{type(data['Industry'])}\t")
            cnt += 1

        self.stdout.write(f"[FINISH] {self.help}", style_func = self.style.SUCCESS, ending = '\n')


def is_stock(data: Series) -> bool:
    """
    콜, 풋, ETF 제외
    """
    if isinstance(data['Sector'], float) and isinstance(data['Industry'], float):
        if math.isnan(data['Sector']) and math.isnan(data['Industry']):
            return True

    return False
