from rest_framework import serializers
from .models import PayrollFormula


class PayrollFormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollFormula
        fields = "__all__"
