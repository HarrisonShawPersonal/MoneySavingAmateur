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
    # Calculate monthly, weekly, and daily values
    monthly_gross_salary = gross_salary / 12
    weekly_gross_salary = gross_salary / 52
    daily_gross_salary = gross_salary / 365

    monthly_ni_contribution = ni_contribution / 12
    weekly_ni_contribution = ni_contribution / 52
    daily_ni_contribution = ni_contribution / 365

    monthly_income_tax = income_tax / 12
    weekly_income_tax = income_tax / 52
    daily_income_tax = income_tax / 365

    monthly_net_salary = net_salary / 12
    weekly_net_salary = net_salary / 52
    daily_net_salary = net_salary / 365

    # Create dictionary with yearly and extended values
    result = {
        'gross_salary': {
            'yearly': gross_salary,
            'monthly': monthly_gross_salary,
            'weekly': weekly_gross_salary,
            'daily': daily_gross_salary,
        },
        'ni_contribution': {
            'yearly': ni_contribution,
            'monthly': monthly_ni_contribution,
            'weekly': weekly_ni_contribution,
            'daily': daily_ni_contribution,
        },
        'income_tax': {
            'yearly': income_tax,
            'monthly': monthly_income_tax,
            'weekly': weekly_income_tax,
            'daily': daily_income_tax,
        },
        'net_salary': {
            'yearly': net_salary,
            'monthly': monthly_net_salary,
            'weekly': weekly_net_salary,
            'daily': daily_net_salary,
        }
    }

    return result