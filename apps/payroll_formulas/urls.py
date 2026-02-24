from django.urls import path
from .views import PayrollFormulaCreateAPIView, PayrollFormulaListAPIView

urlpatterns = [
    path("create/", PayrollFormulaCreateAPIView.as_view()),
    path("", PayrollFormulaListAPIView.as_view()),
]
