from decimal import Decimal


def net(gross_salary):
    gross_salary_decimal = Decimal(str(gross_salary))
    personal_allowance_threshold = Decimal("12570")
    basic_rate_threshold = Decimal("50270")
    higher_rate_threshold = Decimal("125140")
    # income below £12570
    if gross_salary_decimal <= personal_allowance_threshold:
        ni_contribution = 0
        income_tax = 0
    # income greater than £12570 but below £50,270 20%
    elif personal_allowance_threshold < gross_salary_decimal <= basic_rate_threshold:
        income_tax = (gross_salary_decimal - personal_allowance_threshold) * Decimal(
            "0.2"
        )
        ni_contribution = (
            gross_salary_decimal - personal_allowance_threshold
        ) * Decimal("0.08")
    # income greater than £50,270 but below £125,139 40%, below 100k instead
    elif basic_rate_threshold < gross_salary_decimal <= Decimal("100000"):
        income_tax = ((basic_rate_threshold - personal_allowance_threshold) * Decimal("0.2")) + (
            (gross_salary_decimal - basic_rate_threshold ) * Decimal("0.40")
        )
        ni_contribution = Decimal("3016") + (
            (gross_salary_decimal - basic_rate_threshold) * Decimal("0.02")
        )
    # above 100k but less than 125140, with the every £2 personal allowance is reduced by £1
    elif Decimal("100000") < gross_salary_decimal <= higher_rate_threshold:
        income_tax = (
            (gross_salary_decimal - basic_rate_threshold) * Decimal("0.4")
        ) + ((basic_rate_threshold - personal_allowance_threshold) * Decimal("0.2"))
        ni_contribution = Decimal("3016") + (
            (gross_salary_decimal-basic_rate_threshold) * Decimal("0.02")
        )
        # income greater than 125,140 45%
    elif gross_salary_decimal > higher_rate_threshold:
        income_tax = (((basic_rate_threshold - personal_allowance_threshold) * Decimal("0.20")) + ((higher_rate_threshold - basic_rate_threshold + personal_allowance_threshold) * Decimal("0.40"))
        + ((gross_salary_decimal - higher_rate_threshold) * Decimal("0.45")))
        ni_contribution = Decimal("3016") + ((gross_salary_decimal - Decimal("50270")) * Decimal("0.02"))
    else:
        return "Doesn't compute"
    net_salary = gross_salary_decimal - income_tax - ni_contribution
    return ni_contribution, income_tax, net_salary

def breakdown(gross_salary, ni_contribution, income_tax, net_salary):

    monthly_values = [value / 12 for value in (gross_salary, ni_contribution, income_tax, net_salary)]
    weekly_values = [value / 52 for value in (gross_salary, ni_contribution, income_tax, net_salary)]
    daily_values = [value / 260 for value in (gross_salary, ni_contribution, income_tax, net_salary)]

    monthly_values = [round(value, 2) for value in monthly_values]
    weekly_values = [round(value, 2) for value in weekly_values]
    daily_values = [round(value, 2) for value in daily_values]

    result = {
        'gross_salary': {
            'yearly': gross_salary,
            'monthly': monthly_values[0],
            'weekly': weekly_values[0],
            'daily': daily_values[0],
        },
        'ni_contribution': {
            'yearly': ni_contribution,
            'monthly': monthly_values[1],
            'weekly': weekly_values[1],
            'daily': daily_values[1],
        },
        'income_tax': {
            'yearly': income_tax,
            'monthly': monthly_values[2],
            'weekly': weekly_values[2],
            'daily': daily_values[2],
        },
        'net_salary': {
            'yearly': net_salary,
            'monthly': monthly_values[3],
            'weekly': weekly_values[3],
            'daily': daily_values[3],
        }
    }

    return result

def golden_rule(net_salary_monthly):
    wants_percent = Decimal('0.3')
    monthly_needs = int(net_salary_monthly / 2)
    monthly_wants = int(net_salary_monthly * wants_percent)
    monthly_savings = int(net_salary_monthly/ 5)
    golden_rule = {
    "monthly_needs": monthly_needs,
    "monthly_wants": monthly_wants,
    "monthly_savings": monthly_savings
    }
    return golden_rule

def clear_cache():
    print("Does this work")