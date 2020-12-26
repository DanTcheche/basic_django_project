from rest_framework import serializers

from my_project.apps.drf.models import Account, Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'code')
        extra_kwargs = {
            'code': {'validators': []},
        }


class AccountSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    is_developer = serializers.SerializerMethodField()

    class Meta:
        model = Account
        depth = 1
        fields = ('name', 'zip_code', 'address', 'country', 'is_developer')

    def get_is_developer(self, account):
        return account.name.startswith('dev')

    def create(self, validated_data):
        country_data = validated_data.pop('country')
        country, _ = Country.objects.get_or_create(name=country_data['name'],
                                                   code=country_data['code'])
        instance = Account.objects.get_or_create(**validated_data,
                                                 country=country)
        return instance
