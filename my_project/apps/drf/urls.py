from django.urls import path, include

from my_project.apps.drf.views import CountryView, AccountView

urlpatterns = [
    path('countries/', CountryView.as_view(), name="countries_api"),
    path('accounts/', AccountView.as_view(), name="accounts_api"),
]
