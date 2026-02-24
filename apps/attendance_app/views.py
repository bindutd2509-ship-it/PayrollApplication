from rest_framework import generics
from .models import Attendance
from .serializers import AttendanceSerializer


class EmployeeAttendanceListAPIView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        employee_id = self.request.query_params.get("employee_id")
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        queryset = Attendance.objects.filter(employee_id=employee_id)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset