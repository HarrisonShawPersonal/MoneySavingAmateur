from django import forms

class SalaryForm(forms.Form):
    gross_salary = forms.DecimalField(label='Gross Salary')

class NetSalaryForm(forms.Form):
    net_salary = forms.DecimalField(label="Net Salary")