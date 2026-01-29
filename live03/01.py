import requests

def consulta_cep (cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    response = requests.get (url)

    data = response.json()

    print ('#'*20)
    print (f'LOGRADOURO: {data['logradouro']}')
    print (f'LOCALIDADE: {data['localidade']}')
    print (f'ESTADO: {data['estado']}')

cep = input('Digite seu CEP: ')

consulta_cep(cep)