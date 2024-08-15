from django.shortcuts import render
from .models import Transactions
from .serializer import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# @api_view()
# def get_transactions(request):
#     quearyset = Transactions.objects.all()
#     serelizer=TransactionSerializer(quearyset,many=True)
#     return Response({'data':serelizer.data})
class transactions(APIView):
    def get(self,request):
        data=request.data 
        id=data.get('id',None)
        if not id:
            quearyset=Transactions.objects.all()
            serelizer=TransactionSerializer(quearyset,many=True)
            return Response({'data':serelizer.data})
        quearyset=Transactions.objects.get(id=id)
        if not quearyset:
            return Response({'error':'no transaction found'})
        serelizer=TransactionSerializer(quearyset)
        return Response({'data':serelizer.data})
    def post(self,request):
        data=request.data
        serelizer=TransactionSerializer(data=data)
        if serelizer.is_valid():
            serelizer.save()
            return Response({'message':'transaction added',
                             'data':serelizer.data})
        else:
            return Response({'error':serelizer.errors})    
    def put(self,request):
        data=request.data
        id=data.get('id',None)
        if not id:
            return Response({'error':'id is required'})
        else:
            quearyset=Transactions.objects.filter(id=id)
            if not quearyset:
                return Response({'error':'no transaction found'})
            serealizer=TransactionSerializer(quearyset,data=data,partial=True)
            if not serealizer.is_valid():
                return Response({'error':serealizer.errors})
            else:
                serealizer.save()
                return Response({'message':'transaction updated',
                                 'data':serealizer.data})
    def delete(self,request):
        data=request.data
        id=data.get('id',None)
        if not id:
            return Response({'error':'id is required'})
        else:  
            quearyset=Transactions.objects.filter(id=id)
            if not quearyset:
                return Response({'error':'no transaction found'})
            quearyset.delete()
            return Response({'message':'transaction deleted'})