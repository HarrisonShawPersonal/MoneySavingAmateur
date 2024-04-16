from django.urls import path
from . import views

urlpatterns = [
    path("taxcalculator/", views.index, name="index"),
    path("", views.home, name="home"),
    path("budgeter/", views.budget, name="budget")
]
