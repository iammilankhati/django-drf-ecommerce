from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet


app_name = "api-products"


routers = DefaultRouter()
routers.register(r"category", CategoryViewSet, basename="category")


urlpatterns = [
    path("", include(routers.urls)),
]
