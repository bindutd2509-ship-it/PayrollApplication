from django.urls import path
from .views import DepartmentListCreateAPIView

urlpatterns = [
    path('departments/', DepartmentListCreateAPIView.as_view(), name='departments'),
]
