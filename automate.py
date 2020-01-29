import requests

def automate_calc(base_amount):
    ba = str(base_amount)
    response = requests.get('https://us-central1-flask-py-258221.cloudfunctions.net/relo_calc-1', params=(
        ('base_amount', ba),
    ))
    return response.json()
#print(automate_calc(7750.37))
for i in range(7000, 15000, 1000):
    print(automate_calc(i))
