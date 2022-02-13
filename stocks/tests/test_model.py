from django.core.exceptions import ValidationError
from django.test import TestCase

from stocks.models import Market


class MarketModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_create_market_success_case(self):
        # given
        case_market_name = "KOSPI"

        # when
        market = Market.objects.register(case_market_name)

        # then
        self.assertEqual(market.market_name, case_market_name)

    def test_create_market_failure_case(self):
        # given
        case_market_name = "JAY"

        # when
        # then
        with self.assertRaises(ValidationError):
            Market.objects.register(case_market_name)
