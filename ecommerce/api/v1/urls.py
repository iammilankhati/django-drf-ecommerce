from django.urls import path, include

app_name = "api_v1"

urlpatterns = [
    path("product/", include("ecommerce.product.api.v1.urls", namespace="api-products"))
]
