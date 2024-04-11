from django import forms

class SalaryForm(forms.Form):
    gross_amount = forms.IntegerField(label='Gross Amount')
