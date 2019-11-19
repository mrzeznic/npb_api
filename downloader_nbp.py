import requests
import os

url='http://api.nbp.pl/api/exchangerates/tables/a/today/?format=xml'
response = requests.get(url)
file = str(os.path.join(os.path.expanduser("~"), "Desktop")+'\data.xml')

with open(file, 'wb') as f:
    f.write(response.content)
    #f.write(response.text)