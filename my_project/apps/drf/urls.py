from django.urls import path, include
from rest_framework import routers

from my_project.apps.drf.views import CountryView, AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('countries/', CountryView.as_view(), name="countries_api"),
]
