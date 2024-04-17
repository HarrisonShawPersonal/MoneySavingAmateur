from django.shortcuts import render
from  django.http import HttpResponseRedirect
from .forms import *
from .utils import *


def index(request):
    ni_contribution = None
    income_tax = None
    tax_result = None
    net_salary = None
    if 'home' in request.GET:
        response = HttpResponseRedirect('http://127.0.0.1:8000/')
        response.delete_cookie("sessionid")
        return response
    if request.method == "POST":
        form = SalaryForm(request.POST)
        if form.is_valid():
            gross_salary = form.cleaned_data["gross_salary"]
            ni_contribution, income_tax, net_salary = net(gross_salary)
            if ni_contribution is not None and income_tax is not None:
                breakdown_result = breakdown(
                    gross_salary, ni_contribution, income_tax, net_salary
                )
                request.session["net_salary"] = int(breakdown_result['net_salary']['monthly'])

                return render(
                    request,
                    "incometax/index.html",
                    {
                        "form": form,
                        "ni_contribution": ni_contribution,
                        "income_tax": income_tax,
                        "net_salary": net_salary,
                        "gross_salary": gross_salary,
                        "breakdown_result": breakdown_result,
                    },
                )
    else:
        form = SalaryForm()
        return render(request, "incometax/index.html", {"form": form})

def home(request):
    if request.method == "GET":
        return render(request, "incometax/home.html", {})

def budget(request):
    if 'home' in request.GET: 
        response = HttpResponseRedirect("http://127.0.0.1:8000/")
        response.delete_cookie("sessionid")
        return response
    if request.session.get("net_salary") is not None:
        form_monthly = MonthlyCostsForm(request.POST)
        net_salary = request.session.get("net_salary")
        budget = golden_rule(net_salary)
        print (budget)
        return render(
            request,
            "incometax/budget.html",
            {"net_salary": net_salary,
            "budget":budget,
            'form_monthly':form_monthly
            }
        )
    elif "net_salary" in request.POST:
        form = NetSalaryForm(request.POST)
        form_monthly = MonthlyCostsForm(request.POST)
        if form.is_valid():
            net_salary = form.cleaned_data["net_salary"]
            budget = golden_rule(net_salary/12)
            print(budget)
            request.session["budget"] = budget
            return render(request, 'incometax/budget.html', {"form":form , "budget":budget, 'form_monthly':form_monthly})
    elif "monthly_cost" in request.POST:
        form_monthly = MonthlyCostsForm(request.POST)
        if form_monthly.is_valid():
            budget = request.session.get("budget")
            monthly_cost = form_monthly.cleaned_data["monthly_cost"]
            description = form_monthly.cleaned_data["description"]
            category = form_monthly.cleaned_data["category"]
            print(monthly_cost,description,category)
            return render(request, 'incometax/budget.html', {'form_monthly':form_monthly,'budget':budget ,'monthly_cost':monthly_cost,'description':description,'category':category} )


    form = MonthlyCostsForm(request.POST)
    return render(request, 'incometax/budget.html', {'form':form})