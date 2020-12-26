from rest_framework import generics

from my_project.apps.drf.models import Country, Account
from my_project.apps.drf.serializers import CountrySerializer, AccountSerializer


class CountryView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
