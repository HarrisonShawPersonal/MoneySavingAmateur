from django.test import TestCase
from .utils import net, breakdown, golden_rule
from decimal import Decimal

class NetFunctionTests(TestCase):
    
    def test_net_under_12570(self):
        ni_contribution , income_tax , net_salary = net(12570)
        assert ni_contribution == 0 and income_tax == 0 and net_salary == 12570

    def test_net_between_12570_and_50270(self):
        ni_contribution , income_tax , net_salary = net(50270)
        assert ni_contribution == 3016.00 and income_tax == 7540.0 and net_salary == 39714.00
    
    def test_net_between_5270_and_100000(self):
         ni_contribution , income_tax , net_salary = net(70000)
         assert Decimal(ni_contribution) == Decimal("3410.6") and Decimal(income_tax) == Decimal("15432.0") and Decimal(net_salary) == Decimal("51157.4")
    
    def test_net_between_100k_and_125140(self):
        ni_contribution , income_tax , net_salary = net(110000)
        assert Decimal(ni_contribution) == Decimal("4210.6") and Decimal(income_tax) == Decimal("31432.0") and Decimal(net_salary) == Decimal("74357.4")
    
    def test_net_above_125140(self):
        ni_contribution , income_tax , net_salary = net(150000)
        assert Decimal(ni_contribution) == Decimal("5010.6") and Decimal(income_tax) == Decimal("53703.0") and Decimal(net_salary) == Decimal("91286.4")

class GoldenRuleFunctionTests(TestCase):

    def test_expected_results(self):
        expected_result = {
            "monthly_needs": 1500,
            "monthly_wants": 900,
            "monthly_savings": 600
        }
        assert golden_rule(3000) == expected_result