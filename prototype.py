from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import pprint

json_result = {}
datetime_string = '08/23/2019'
tax_percentage = 0.466
def string_to_datetime(string_datetime, string_format):
    datetime_object = datetime.strptime(string_datetime, string_format)
    return datetime_object
def datetime_to_string(datetime_object, string_format):
    string_datetime = datetime_object.strftime(string_format)
    return string_datetime
datetime_object = string_to_datetime(datetime_string, '%m/%d/%Y')
base_amount = 7750.37
def calculate_tax(base_amount, tax_percentage=0.466):
    tax_amount = base_amount * tax_percentage
    return tax_amount
def add_months(datetime_object, number_of_months):
    print("Month: {}".format(number_of_months))
    time_delta_calc = relativedelta(months=number_of_months)
    new_datetime_object = datetime_object + time_delta_calc
    return new_datetime_object
def monthly_amount(total_12_months):
    return total_12_months/12
def due_amount(monthly_amount, month, total_12_months):
    disbursable = monthly_amount * month
    return total_12_months - disbursable
business_relocation_date = datetime_to_string(datetime_object,'%m-%d-%Y')
print("Business Relocation Date: {}".format(business_relocation_date))
json_result['business_relocation_date'] = business_relocation_date
print("Tax: {}%".format(tax_percentage*100))
json_result['tax_percentage'] = tax_percentage*100
print("Base Amount: ", base_amount)
json_result['base_amount'] = base_amount
tax_gross = calculate_tax(base_amount)
json_result['tax_gross'] = tax_gross
print("Tax Gross: ", tax_gross)
total_12_months = base_amount + tax_gross
json_result['total_amount'] = total_12_months
print("Total Amount: ", total_12_months)
monthly_disbursable = monthly_amount(total_12_months)
json_result['monthly_disbursable'] = monthly_disbursable
print("Monthly Amount: ", monthly_disbursable)
monthly_disbursable_amount = []
for i in range(12+1):
    i_date = datetime_to_string(add_months(datetime_object, i), '%m-%d-%Y')
    amount_due = due_amount(monthly_disbursable, i, total_12_months)
    print(i_date, amount_due)
    monthly_disbursable_amount.append({'date': i_date,'amount_due': amount_due})
print(monthly_disbursable_amount)
json_result['monthly_disbursable_amount'] = monthly_disbursable_amount
pprint.pprint(json_result)
