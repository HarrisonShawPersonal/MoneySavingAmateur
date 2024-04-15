from django import forms

class SalaryForm(forms.Form):
    gross_salary = forms.DecimalField(label='Gross Salary')
