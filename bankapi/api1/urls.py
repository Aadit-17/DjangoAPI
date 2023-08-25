from django.contrib import admin
from django.urls import path, include
from api1.views import BankViewSet, CustomerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
]