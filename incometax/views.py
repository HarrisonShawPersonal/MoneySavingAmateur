from django.shortcuts import render
from .forms import SalaryForm
from .utils import net, breakdown

def index(request):
    ni_contribution = None
    income_tax = None
    tax_result = None
    net_salary =None
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            gross_salary = form.cleaned_data['gross_salary']
            ni_contribution , income_tax , net_salary = net(gross_salary)
            print(ni_contribution , income_tax)
            if ni_contribution is not None and income_tax is not None:
                breakdown_result = breakdown(gross_salary, ni_contribution, income_tax, net_salary)
                return render(request, 'incometax/index.html',{'form':form,'ni_contribution':ni_contribution,'income_tax':income_tax, 'net_salary':net_salary ,'gross_salary':gross_salary,'breakdown_result':breakdown_result})
    else:
        form = SalaryForm()
        return render(request,'incometax/index.html',{'form':form})

    

def home(request):
    if request.method == 'GET':
        return render(request, 'incometax/home.html',{})
