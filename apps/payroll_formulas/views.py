from rest_framework import generics
from .models import PayrollFormula
from .serializers import PayrollFormulaSerializer


class PayrollFormulaCreateAPIView(generics.CreateAPIView):
    queryset = PayrollFormula.objects.all()
    serializer_class = PayrollFormulaSerializer


class PayrollFormulaListAPIView(generics.ListAPIView):
    serializer_class = PayrollFormulaSerializer

    def get_queryset(self):
        company_id = self.request.query_params.get("company_id")
        return PayrollFormula.objects.filter(company_id=company_id)
