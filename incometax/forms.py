from django import forms


class SalaryForm(forms.Form):
    gross_salary = forms.DecimalField(label="Gross Salary")


class NetSalaryForm(forms.Form):
    net_salary = forms.DecimalField(label="Net Salary")


class MonthlyCostsForm(forms.Form):
    monthly_cost = forms.DecimalField(label="Monthly Cost")
    description = forms.CharField(max_length=200, label="Description")
    CATEGORY_CHOICES = [
        ("wants", "Wants"),
        ("needs", "Needs"),
        ("savings", "Savings"),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
