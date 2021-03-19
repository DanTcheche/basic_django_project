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
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Country.objects)
    is_developer = serializers.SerializerMethodField()

    class Meta:
        model = Account
        depth = 1
        fields = ('name', 'zip_code', 'address', 'country', 'country_id', 'is_developer', )
        read_only_fields = ('country', )

    def get_is_developer(self, account):
        return account.name.startswith('dev')

    def create(self, validated_data):
        validated_data['country_id'] = validated_data['country_id'].id
        return super().create(validated_data)
