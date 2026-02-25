from django.urls import path
from .views import RoleCreateAPIView, RoleListAPIView

urlpatterns = [
    path("create/", RoleCreateAPIView.as_view(), name="create-role"),
    path("", RoleListAPIView.as_view(), name="list-roles"),
]
