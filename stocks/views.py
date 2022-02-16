from django.shortcuts import render
from django.http import HttpRequest

from django.views import View
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from stocks.models import Industry
from stocks.serializers import IndustryStockSerializer


class StockViews(View):
    template_name = 'stock/stock_index.html'
    page_title = 'Stock'

    def get(self, request: HttpRequest):
        return render(request, self.template_name, {
            'page_title': self.page_title,
        })


class IndustryStockListAPIView(APIView):

    def get(self, request: Request):
        industry = Industry.objects.prefetch_related('industry_stocks').all()
        serializer = IndustryStockSerializer(industry, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
#
#     def post(self, request: Request):
#         serializer = IndustryStockSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
