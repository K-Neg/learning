import requests

url = "http://www.cepaberto.com/api/v3/cep?cep=13520000"
headers = {'Authorization': 'Token token=xxxxx'}
response = requests.get(url, headers=headers)

print(response.json())