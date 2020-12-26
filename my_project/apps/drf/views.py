from rest_framework import generics

from my_project.apps.drf.models import Account
from my_project.apps.drf.serializers import AccountSerializer


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
