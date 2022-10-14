import requests
import json
from os import system, name
# Preencher os dados
# URL Ponto de extremidade
urlApi="URL_DA_API"
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Texto para envio, alterar os dados para enviar
dadosEnvio = {
  "Inputs": { 
    "data": [
      {
        "day": 4,           # dia do mês
        "mnth": 10,         # mês  
        "year": 2022,       # ano
        "season": 1,        # estação do ano 1-primavera, 2-verão, 3-outono, 4-inverno
        "holiday": 0,       # feriado 0 - não, 1 - sim
        "weekday": 2,       # dia da semana 0-dom,1-seg,2-ter,3-qua,4-qui,5-sex,6-sab
        "workingday": 1,    # dia de trabalho 0-não, 1-sim
        "weathersit": 1,    # situação do tempo 1-tempo bom,2-nublado, 3-chuva leve, 4-chuva forte
        "temp": 26.0,       # temperatura em graus celsius
        "atemp": 26.0,      # sensação térmica em graus celsius
        "hum": 60.0,        # umidade relativa do ar em percentual
        "windspeed": 15.0   # velocidade do vento em km/s
      }
    ]    
  },   
  "GlobalParameters": 1.0
}
# Função para limpar a tela
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")
# Montando o cabeção de envio
cabecalhoEnvio = { "Content-Type" : "application/json", "Authorization": f"Bearer {chave}" }
# Realizando a requisição do serviço
retorno = requests.post(urlApi, json=dadosEnvio, headers=cabecalhoEnvio)
# Limpando a tela
clear()
# Imprimindo o resultado
print("Previsão de Locação de Bicicletas: " + str(retorno.json()["Results"][0]))
print("-" * 40)
print(json.dumps(retorno.json(),indent=3))