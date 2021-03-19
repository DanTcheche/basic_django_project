from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from my_project.apps.drf.models import Country, Account
from my_project.apps.drf.serializers import CountrySerializer, AccountSerializer


class CountryView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

