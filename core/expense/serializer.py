from rest_framework import serializers
from .models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transactions
        fields='__all__'
        #exclude=['id'] #excludes the perticular field from serialization