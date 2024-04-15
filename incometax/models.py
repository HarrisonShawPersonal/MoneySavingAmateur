from typing import Any
from django.db import models


class Salary(models.Model):
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return str(self.gross_amount)

class TaxCalculationResult(models.Model):
    ni_contribution = models.DecimalField(max_digits=10, decimal_places=2)
    income_tax = models.DecimalField(max_digits=10, decimal_places=2)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)