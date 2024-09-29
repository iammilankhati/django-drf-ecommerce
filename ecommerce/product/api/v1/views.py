from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied

from ecommerce.product.models import Category
from .serializers import CategorySerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all categories",
        description="Retrieve a list of all categories with detailed information.",
        tags=["Categories"],  # Categories tag for grouping
        responses={200: CategorySerializer(many=True)},  # Define response schema
        # exclude=False,
    ),
    create=extend_schema(
        summary="Create a new category",
        description="Create a new category with the provided data.",
        tags=["Categories"],
        request=CategorySerializer,  # Request body for creating category
        responses={201: CategorySerializer},  # Define response schema
        # exclude=False,
    ),
)
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing category
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == "list":
            # Public API, anyone can access
            self.permission_classes = [AllowAny]
        elif self.action == "create":
            # Private API, restricted to super admin only
            self.permission_classes = [IsAuthenticated]
            if not self.request.user.is_superuser:
                raise PermissionDenied("Only super admins can create categories.")
        return super().get_permissions()

    def list(self, request):
        print("listing", request.user)
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
