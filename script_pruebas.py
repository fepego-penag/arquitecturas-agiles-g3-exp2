import requests


historia_clinica_responses = []
for i in range(100):
    response = requests.get('http://localhost:5000/historia_clinica/10')
    if response.status_code == 200:
        historia_clinica_responses.append(response)
assert not historia_clinica_responses


reportes_responses = []
for i in range(100):
    response = requests.get('http://localhost:5000/reportes/5')
    if response.status_code == 200:
        reportes_responses.append(response)
assert not reportes_responses


historia_clinica_responses = []
for i in range(100):
    response = requests.get('http://localhost:5000/historia_clinica/10', headers={'usuario': 'medico'})
    if response.status_code == 200:
        token = response.json()['access_token']
        response = requests.get('http://localhost:5000/historia_clinica/10', headers={'Authorization': f'Bearer {token}'})
        if response.status_code == 200 and response.json() == 'datos de historia clínica 10':
            historia_clinica_responses.append(response)
assert len(historia_clinica_responses) == 100


reportes_responses = []
url = 'http://localhost:5000/reportes/5'
for i in range(100):
    response = requests.get(url, headers={'usuario': 'finanzas'})
    if response.status_code == 200:
        token = response.json()['access_token']
        response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
        if response.status_code == 200 and response.json() == 'procesando reporte 5':
            reportes_responses.append(response)
assert len(reportes_responses) == 100


historia_clinica_responses = []
url = 'http://localhost:5000/historia_clinica/10'
for i in range(100):
    response = requests.get(url, headers={'usuario': 'finanzas'})
    if response.status_code == 200:
        token = response.json()['access_token']
        response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
        if response.status_code == 200 and response.json() == 'datos de historia clínica 10':
            historia_clinica_responses.append(response)
assert len(historia_clinica_responses) == 0



reportes_responses = []
url = 'http://localhost:5000/reportes/5'
for i in range(100):
    response = requests.get(url, headers={'usuario': 'medico'})
    if response.status_code == 200:
        token = response.json()['access_token']
        response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
        if response.status_code == 200 and response.json() == 'procesando reporte 5':
            reportes_responses.append(response)
assert len(reportes_responses) == 0