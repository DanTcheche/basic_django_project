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

    def create(self, request, *args, **kwargs):
        account_name = self.request.data.get('name')
        zip_code = self.request.data.get('zip_code')
        address = self.request.data.get('address')
        country_id = self.request.data.get('country_id')
        country = Country.objects.filter(id=country_id).first()
        if not country:
            return Response("Country not found", status=404)
        if account_name:
            account = Account.objects.create(name=account_name,
                                             country=country,
                                             zip_code=zip_code,
                                             address=address)
            serializer = self.get_serializer(instance=account)
            return Response(serializer.data, status=201)
        return Response("Missing account name", status=400)
