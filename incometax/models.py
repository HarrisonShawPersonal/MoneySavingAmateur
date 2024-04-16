from typing import Any
from django.db import models


class Salary(models.Model):
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return str(self.gross_amount)

class TaxCalculationResult(models.Model):
    ni_contribution = models.DecimalField(max_digits=10, decimal_places=2)
    income_tax = models.DecimalField(max_digits=10, decimal_places=2)

class NetSalary(models.Model):
    net_salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)        