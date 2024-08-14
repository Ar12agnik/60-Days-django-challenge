from django.shortcuts import render
from .models import Transactions
from .serializer import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view()
def get_transactions(request):
    quearyset = Transactions.objects.all()
    serelizer=TransactionSerializer(quearyset,many=True)
    return Response({'data':serelizer.data})