import uuid
from django.db import models


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PayrollFormula(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="payroll_formulas"
    )

    name = models.CharField(max_length=150)
    formula_expression = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payroll_formulas"
        unique_together = ("company", "name")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.company.name}"
