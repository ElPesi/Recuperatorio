import requests, json

startVocal = []
startCons = []
print('Elije una cantidad de usarios entre 1 y 10')
cantUsers = int(input())

if cantUsers > 0 and cantUsers < 11:
    url = f'https://jsonplaceholder.typicode.com/users' 
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        for i in range(cantUsers):
            if data[i]['name'].startswith('A') or  data[i]['name'].startswith('E') or  data[i]['name'].startswith('I') or  data[i]['name'].startswith('O') or  data[i]['name'].startswith('U'): 
                startVocal.append(data[i])
            else:
                startCons.append(data[i])
    else:
        print(f'Error {response.status_code}')
else:
    print('Cantidad de usuarios invalidad, selecione un numero entre 1 y 10')
    cantUsers = int(input())
    
print(f'Los post de personas cuyo nombre empiece con vocal: {startVocal}')
print(f'Los post de personas cuyo nombre empiece con consonante: {startCons}')

with open('./UserData/usersConsonants.json','w') as archivo: json.dump('startVocal', 'archivo')
with open('./UserData/usersVowels.json','w') as archivo: json.dump('startVocal', 'archivo')