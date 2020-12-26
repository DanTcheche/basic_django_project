from rest_framework import serializers

from my_project.apps.drf.models import Account, Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'code')


class AccountSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    is_developer = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('name', 'zipcode', 'address', 'country')

    def get_is_developer(self, account):
        return account.name.startswith('dev')
