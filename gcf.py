from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from flask import escape, jsonify

class reloc_calc:
    json_result = {}
    def __init__(self, datetime_string = '08/23/2019', tax_percentage = 0.466, base_amount = 1000, time_format='%m/%d/%Y'):
        self.datetime_string = datetime_string
        self.tax_percentage = tax_percentage
        self.base_amount = base_amount
        self.time_format = time_format
        self.datetime_object = self.string_to_datetime(self.datetime_string, self.time_format)

    def string_to_datetime(self, string_datetime, string_format):
    	datetime_object = datetime.strptime(string_datetime, string_format)
    	return datetime_object

    def datetime_to_string(self, datetime_object, string_format):
    	string_datetime = datetime_object.strftime(string_format)
    	return string_datetime

    def calculate_tax(self, base_amount, tax_percentage=0.466):
    	tax_amount = base_amount * tax_percentage
    	return tax_amount

    def add_months(self, datetime_object, number_of_months):
    	time_delta_calc = relativedelta(months=number_of_months)
    	new_datetime_object = datetime_object + time_delta_calc
    	return new_datetime_object

    def monthly_amount(self, total_12_months):
    	return total_12_months/12

    def due_amount(self, monthly_amount, month, total_12_months):
    	disbursable = monthly_amount * month
    	return total_12_months - disbursable

    def get(self):
    	business_relocation_date = self.datetime_to_string(self.datetime_object,'%m-%d-%Y')
    	self.json_result['business_relocation_date'] = business_relocation_date
    	self.json_result['tax_percentage'] = self.tax_percentage*100
    	self.json_result['base_amount'] = self.base_amount
    	tax_gross = self.calculate_tax(self.base_amount)
    	self.json_result['tax_gross'] = tax_gross
    	total_12_months = self.base_amount + tax_gross
    	self.json_result['total_amount'] = total_12_months
    	monthly_disbursable = self.monthly_amount(total_12_months)
    	self.json_result['monthly_disbursable'] = monthly_disbursable
    	monthly_disbursable_amount = []
    	for i in range(12+1):
    		i_date = self.datetime_to_string(self.add_months(self.datetime_object, i), '%m-%d-%Y')
    		amount_due = self.due_amount(monthly_disbursable, i, total_12_months)
    		monthly_disbursable_amount.append({'date': i_date,'amount_due': amount_due})
    	self.json_result['monthly_disbursable_amount'] = monthly_disbursable_amount
    	return self.json_result

def relo_calc(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'base_amount' in request_json:
        base_amount = request_json['base_amount']
    elif request_args and 'base_amount' in request_args:
        base_amount = request_args['base_amount']
    else:
        base_amount = 1000
    rc = reloc_calc(base_amount = base_amount).get()
    final_val = jsonify(rc)
    return final_val
