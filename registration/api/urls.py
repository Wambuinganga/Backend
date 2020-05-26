from rest_framework import routers
from .views import AccountViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]