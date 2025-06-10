import requests
from arquiLib import *

# Recebe a chave externa
api_file = 'Qualidade do ar/chave.txt'

if file_exists(api_file) == True:
    # Entrada da usuario
    cidade = str(input('Digite o nome da cidade: ')).lower().strip()

    #Chave da API
    with open(api_file, 'r', encoding='utf-8') as fl:
        api_key = fl.read()

    #URL da API com a cidade inserida
    url = f"https://api.api-ninjas.com/v1/airquality?city={cidade}"
    headers = {"X-Api-Key": api_key} 

    # Requisição GET á API
    try:
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status() # Levanta um erro caso a requisição falhe
    except requests.exceptions.RequestException as erro:
        print(f'Erro na requisição: {erro}')
        exit()

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        
        print(f"\n   Qualidade do ar em {cidade.capitalize()}:")
        print(f" - Índice Geral (AQI): {dados['overall_aqi']}")
        if 'PM2.5' in dados and 'concentration' in dados['PM2.5']:
            print(f" - O nível de partículas PM2.5 é {dados['PM2.5']['concentration']:.2f}")
        else:
            print(' - Dados de PM2.5 não disponiveis.')
        print(f" - Dióxido de Nitrogênio (NO2): {dados['NO2']['concentration']:.2f}")
        print(f" - Ozônio (O3): {dados['O3']['concentration']:.2f}")
    else:
        print("  Não foi possível obter os dados. Verifique a cidade ou sua chave de API.")