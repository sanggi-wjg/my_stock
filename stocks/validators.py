from django.core.exceptions import ValidationError

from my_stock.constants import ALLOW_MARKETS


def validate_allow_market_name(market_name: str):
    if market_name not in ALLOW_MARKETS:
        raise ValidationError(f"market name({market_name}) is not allowed")
