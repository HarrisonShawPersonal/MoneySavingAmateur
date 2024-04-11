from django.db import models


class Salary(models.Model):
    gross_amount = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.gross_amount)
