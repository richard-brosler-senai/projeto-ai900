import requests
import json
from os import system, name
# Preencher os dados
# URL Ponto de extremidade
urlApi="URL_API"
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Texto para envio, alterar os dados para enviar
dadosEnvio =  {
   "Inputs": {
     "WebServiceInput0":
       [
         { "PatientID": 1882185,          # ID do paciente
           "Pregnancies": 9,              # Meses de gravidez
           "PlasmaGlucose": 104,          # Glicose
           "DiastolicBloodPressure": 51,  # Pressão Diastólica
           "TricepsThickness": 7,         # Espessura do tríceps
           "SerumInsulin": 24,            # Insulina sérica
           "BMI": 27.36983156,            # IMC
           "DiabetesPedigree": 1.3504720469999998, # Linhagem de Diabetes
           "Age": 43                      # Idade
          }
        ]
       },
   "GlobalParameters":  {}
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
infoPaciente = retorno.json()["Results"]["WebServiceOutput0"][0]
print("Paciente : " + str(infoPaciente["PatientID"]))
print("Terá Diabetes? : " + ("Sim" if infoPaciente["DiabetesPrediction"]==1 else "Não"))
print("Probabilidades de Diabetes: " + str(infoPaciente["Probability"]))
print("-" * 40)
print(json.dumps(retorno.json(),indent=3))