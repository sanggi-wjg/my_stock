from io import StringIO
from unittest import skipIf

from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.test import TestCase

from stocks.management.commands import register_stocks


class RegisterStocksCommandTestCase(TestCase):
    """
    https://adamj.eu/tech/2020/09/07/how-to-unit-test-a-django-management-command/
    """

    def setUp(self) -> None:
        self.command = register_stocks.Command()

    def call_command(self, *args, **kwargs):
        call_command("register_stocks", *args, stdout = StringIO(), stderr = StringIO(), **kwargs)

    def test_command_options(self):
        with self.assertRaises(ValidationError):
            self.command.initialize(market_name = "삼성전자")
        self.command.initialize(market_name = "KOSPI")

        self.assertEqual(self.command.market.market_name, "KOSPI")

    @skipIf(True, "Just test on local")
    def test_register_stocks_success_case(self):
        market_name = "KOSPI"
        call_command(market_name)
