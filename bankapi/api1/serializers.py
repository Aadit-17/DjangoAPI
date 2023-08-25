from rest_framework import serializers
from .models import Bank, Customer
# create serializers


class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = "__all__"
