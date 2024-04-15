from .models import TaxCalculationResult
from decimal import Decimal

def net(gross_salary):
    gross_salary_decimal = Decimal(str(gross_salary))
    personal_allowance_threshold = Decimal("12570")
    basic_rate_threshold = Decimal("50270")
    higher_rate_threshold = Decimal("125140")
    #income below £12570
    if gross_salary_decimal <= personal_allowance_threshold:
        ni_contribution = 0
        income_tax = 0
    #income greater than £12570 but below £50,270 20%
    elif personal_allowance_threshold < gross_salary_decimal <= basic_rate_threshold:
        income_tax = (gross_salary_decimal-personal_allowance_threshold) * Decimal("0.2")
        ni_contribution = (gross_salary_decimal-personal_allowance_threshold) * Decimal("0.08")
        # return "You pay no tax on the first £12570, but you pay 20% on the remaining £{}".format(
        #     gross_amount - 12570
        #)
    #income greater than £50,270 but below £125,139 40%, below 100k instead
    elif basic_rate_threshold < gross_salary_decimal <= Decimal("100000"):
        income_tax = (gross_salary_decimal-personal_allowance_threshold *Decimal("0.2")) + (gross_salary_decimal-(basic_rate_threshold - personal_allowance_threshold) * Decimal("0.40"))
        ni_contribution =Decimal("3016") + ((gross_salary_decimal - basic_rate_threshold) * Decimal("0.02"))
        # return "You pay no tax on the first £12570, you will pay 20% on the next £37700 and you will pay 40% on £{}".format(
        #     gross_amount - 50270
        #)
        # above 100k but less than 125140, with the every £2 personal allowance is reduced by £1
    elif Decimal("100000") < gross_salary_decimal <= higher_rate_threshold:
        income_tax = ((gross_salary_decimal - basic_rate_threshold) * Decimal("0.4")) + ((gross_salary_decimal - basic_rate_threshold - (gross_salary - basic_rate_threshold)) * Decimal("0.2"))
        ni_contribution = Decimal("3016") + ((gross_salary_decimal - basic_rate_threshold) * Decimal("0.02"))
        #income greater than 125,140 45% 
    elif gross_salary_decimal > higher_rate_threshold:
        income_tax = (basic_rate_threshold * Decimal("0.20")) + ((higher_rate_threshold-basic_rate_threshold) * Decimal("0.4")) +  ((gross_salary_decimal-higher_rate_threshold) * Decimal("0.45"))
        ni_contribution = Decimal("3016") + ((gross_salary_decimal - Decimal("50270")) * Decimal("0.02"))
        # return "You pay no tax on the first £12570, you will pay 20% on the next £37700 and you will pay 40% on the next £74868 and then 45% on £{}".format(
        #     gross_amount - 125140
        # )
    else:
        return "Doesn't compute"
    return ni_contribution,income_tax