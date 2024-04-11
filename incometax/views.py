from django.shortcuts import render
from .forms import SalaryForm
from .utils import net

def index(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            gross_amount = form.cleaned_data['gross_amount']
            net_amount = net(gross_amount)
            return render(request, 'incometax/index.html', {'form': form, 'net_amount': net_amount})
    else:
        form = SalaryForm()
    return render(request, 'incometax/index.html', {'form': form})
