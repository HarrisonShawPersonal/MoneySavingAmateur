def net(gross_amount):
    #income below £12570
    if gross_amount - 12570 < 0:
        ni_contribution = 0
        income_tax = 0
        return "You pay no tax"
    #income greater than £12570 but below £50,270 20%
    elif gross_amount - 12570 < 37700:
        income_tax = (gross_amount-12570) * 0.2
        ni_contribution = (gross_amount-12570) * 0.08
        return "You pay no tax on the first £12570, but you pay 20% on the remaining £{}".format(
            gross_amount - 12570
        )
    #income greater than £50,270 but below £125,139 40%
    elif 112569 > gross_amount - 12570 > 37700:
        income_tax = (gross_amount-12570 *0.2)+(gross_amount-37700*40)
        ni_contribution =3016
        return "You pay no tax on the first £12570, you will pay 20% on the next £37700 and you will pay 40% on £{}".format(
            gross_amount - 50270
        )
    #income greater than 125,140 45%
    elif gross_amount > 125140:
        return "You pay no tax on the first £12570, you will pay 20% on the next £37700 and you will pay 40% on the next £74868 and then 45% on £{}".format(
            gross_amount - 125140
        )
    else:
        return "Doesn't compute"
