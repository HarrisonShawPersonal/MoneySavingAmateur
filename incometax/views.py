from django.shortcuts import render
from .forms import SalaryForm
from .utils import net
from .models import TaxCalculationResult

def index(request):
    ni_contribution = None
    income_tax = None
    tax_result = None

    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            gross_salary = form.cleaned_data['gross_salary']
            ni_contribution , income_tax = net(gross_salary)
            print(ni_contribution , income_tax)
            if ni_contribution is not None and income_tax is not None:
                return render(request, 'incometax/index.html',{'form':form,'ni_contribution':ni_contribution,'income_tax':income_tax})
                tax_result = TaxCalculationResult.objects.create(ni_contribution=ni_contribution, income_tax=income_tax)
    else:
        form = SalaryForm()

    return render(request, 'incometax/index.html', {'form': form, 'tax_result': tax_result})
