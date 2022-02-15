from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from rest_framework.test import APIRequestFactory


class MarketViewTestCase(TestCase):

    def test_market_lists(self):
        # given
        # when
        # then
        factory = APIRequestFactory()
        request = factory.get('/v1/markets')
        request.user = AnonymousUser()

