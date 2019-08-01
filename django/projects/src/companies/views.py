from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from. serializers import StockSerializer

# Create your views here.
class StockList(APIView):
	# Consult Stock List
	def get(self, request):
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)

	# Create a New Stock
	def post(self):
		pass