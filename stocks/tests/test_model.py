from django.core.exceptions import ValidationError
from django.test import TestCase

from stocks.models import Market, Sector, Industry, Stock
from stocks.validators import validate_allow_market_name


class MarketModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_validator_validate_allow_market_name_success_case(self):
        # given
        market_name = "KOSPI"

        # when
        # then
        validate_allow_market_name(market_name)

    def test_validator_validate_allow_market_name_failure_case(self):
        # given
        market_name = "Snow"

        # when
        # then
        with self.assertRaises(ValidationError):
            validate_allow_market_name(market_name)

    def test_create_market_success_case(self):
        # given
        market_name = "KOSPI"

        # when
        market = Market.objects.register(market_name)

        # then
        self.assertEqual(market.market_name, market_name)

    def test_create_market_failure_case(self):
        # given
        market_name = "JAY"

        # when
        # then
        with self.assertRaises(ValidationError):
            Market.objects.register_if_not_exist(market_name)


class SectorModelTestCase(TestCase):

    def test_create_sector_success_case(self):
        # given
        sector_name = "산업"

        # when
        sector = Sector.objects.register_if_not_exist(sector_name)

        # then
        self.assertEqual(sector.sector_name, sector_name)


class IndustryModelTestCase(TestCase):

    def test_create_industry_success_case(self):
        # given
        industry_name = "반도체"

        # when
        industry = Industry.objects.register_if_not_exist(industry_name)

        # then
        self.assertEqual(industry.industry_name, industry_name)


class StockModelTestCase(TestCase):

    def setUp(self) -> None:
        self.market = Market.objects.register_if_not_exist("KOSPI")
        self.sector = Sector.objects.register_if_not_exist("반도체, 핸드폰")
        self.industry = Industry.objects.register_if_not_exist("전자기기")

    def test_create_stock_success_case(self):
        # given
        stock_code, stock_name = "123456", "삼성전자"

        # when
        stock = Stock.objects.register_if_not_exist(
            Stock(market = self.market, sector = self.sector, industry = self.industry, stock_code = stock_code, stock_name = stock_name)
        )

        # then
        self.assertEqual(stock.stock_code, stock_code)
        self.assertEqual(stock.stock_name, stock_name)

    def test_create_stock_failure_case(self):
        # given
        stock_code, stock_name = "123456", "삼성전자"

        # when
        # then
        with self.assertRaises(ValidationError):
            Stock.objects.register_if_not_exist(
                Stock(sector = self.sector, industry = self.industry, stock_code = stock_code, stock_name = stock_name)
            )
        with self.assertRaises(ValidationError):
            Stock.objects.register_if_not_exist(
                Stock(market = self.market, industry = self.industry, stock_code = stock_code, stock_name = stock_name)
            )
        with self.assertRaises(ValidationError):
            Stock.objects.register_if_not_exist(
                Stock(market = self.market, sector = self.sector, stock_code = stock_code, stock_name = stock_name)
            )
