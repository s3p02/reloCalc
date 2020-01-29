from relo_calc import relo_calc
import unittest

class test_relo_calc(unittest.TestCase):
    base_amount = 7750.37
    business_relocation_date = '08-23-2019'
    monthly_disbursable = 946.8368683333333
    tax_gross = 3611.6724200000003
    tax_percentage = 46.6
    total_amount = 11362.04242
    def test_get(self):
        rc = relo_calc.reloc_calc(datetime_string = '08/23/2019',
        tax_percentage = self.tax_percentage/100,
        base_amount = self.base_amount,
        time_format='%m/%d/%Y')
        result = rc.get()
        self.assertNotEqual(result, {})
        self.assertEqual(result['base_amount'], self.base_amount)
        self.assertEqual(result['monthly_disbursable'],
        self.monthly_disbursable)
        self.assertEqual(result['tax_gross'], self.tax_gross)
        self.assertEqual(result['tax_percentage'], self.tax_percentage)
        self.assertEqual(result['total_amount'], self.total_amount)

if __name__ == "__main__":
    unittest.main()
