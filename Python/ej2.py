import requests, json

print('Elija la ciudad del post')
city = input()
print(f'Ciudad elejida {city}')

url = f'https://jsonplaceholder.typicode.com/users' 
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print('adf')
    for i in range(0, 10):
        if city == data[i]['address']['city']:
            print(f'El post solicitado es: {data[i]['address']['city']}')
            
else:
    print(f'Error {response.status_code}')
