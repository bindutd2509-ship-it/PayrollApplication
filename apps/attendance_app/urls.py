from django.urls import path
from .views import EmployeeAttendanceListAPIView

urlpatterns = [
    path("employee/", EmployeeAttendanceListAPIView.as_view()),
]