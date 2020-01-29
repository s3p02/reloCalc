import requests
import json
import sys
from multiprocessing import Pool

try:
    base_path = sys.argv[1]
except IndexError:
    print("path needed! eg: /path/to/save")
    sys.exit(1)

def automate_calc(base_amount):
    ba = str(base_amount)
    response = requests.get('https://us-central1-flask-py-258221.cloudfunctions.net/relo_calc-1', params=(
        ('base_amount', ba),
    ))
    return response.json()
#print(automate_calc(7750.37))
#for i in range(7000, 15000, 1000):
def fetchNwrite(i):
    fname = base_path + '/' + '{}.json'.format(i)
    print(fname)
    a = automate_calc(i)
    print(a)
    with open(fname, 'w') as json_file:
        json.dump(a, json_file)
walk = range(7000, 15000, 1000)
p = Pool(5)
p.map(fetchNwrite, walk)
#https://docs.python.org/2/library/multiprocessing.html
