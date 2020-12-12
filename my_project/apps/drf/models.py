from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3, blank=True, null=True, unique=True)


class Account(models.Model):
    name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, related_name='accounts', on_delete=models.PROTECT, blank=True, null=True)


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    account = models.ForeignKey(Account, related_name='users', on_delete=models.CASCADE, blank=True, null=True)
