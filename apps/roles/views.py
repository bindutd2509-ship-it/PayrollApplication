from rest_framework import generics
from .models import Role
from .serializers import RoleSerializer


class RoleCreateAPIView(generics.CreateAPIView):
    """
    Create a new role
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleListAPIView(generics.ListAPIView):
    """
    List roles by company_id
    """
    serializer_class = RoleSerializer

    def get_queryset(self):
        company_id = self.request.query_params.get("company_id")
        return Role.objects.filter(company_id=company_id)
