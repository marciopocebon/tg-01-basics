import requests

api_key = 'asdf1234asdf1234asdf1234'

url = 'https://panacea.threatgrid.com/api/v3/configuration/vms?api_key={}'.format(api_key)

r = requests.get(url)

print(r.json())