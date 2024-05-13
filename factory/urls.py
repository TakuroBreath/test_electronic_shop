from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import FactoryConfig
from .views import NetworkNodeViewSet, ProductViewSet

app_name = FactoryConfig.name

router = DefaultRouter()

router.register(r'networknodes', NetworkNodeViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
