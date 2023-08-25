from django.shortcuts import render
from rest_framework import viewsets
from api1.models import Bank, Customer
from api1.serializers import BankSerializer, CustomerSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
# Create your views here.


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    @action(detail=True, methods=['get'])
    def customers(self, request, pk=None):
        try:
            bank_n = Bank.objects.get(pk=pk)
            emps = Customer.objects.filter(bank=bank_n)
            cust_serializer = CustomerSerializer(emps, many=True, context={'request': request})
            return Response(cust_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message': 'Company does not exist.'})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
