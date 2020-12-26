from django.urls import path, include

from my_project.apps.drf.views import AccountView

urlpatterns = [
    path('accounts/', AccountView.as_view(), name="accounts_api"),
]
