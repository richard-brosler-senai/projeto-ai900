import requests
# Preencher os dados
# URL Ponto de extremidade
urlApi="http://acb91ea8-a25f-42e5-adf9-e3d9e04b3ef7.brazilsouth.azurecontainer.io/score"
# Chave Primária de autenticacao
chave = "xsW7wRxNeIzVR3Et4qKcDTqlL47Uz6FY"
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
# Montando o cabeção de envio
cabecalhoEnvio = { "Content-Type" : "application/json", "Authorization": f"Bearer {chave}" }
# Realizando a requisição do serviço
retorno = requests.post(urlApi, json=dadosEnvio, headers=cabecalhoEnvio)
# Limpando a tela
print(chr(27) + "[2J") 
# Imprimindo o resultado
infoPaciente = retorno.json()["Results"]["WebServiceOutput0"][0]
print("Paciente : " + str(infoPaciente["PatientID"]))
print("Terá Diabetes? : " + ("Sim" if infoPaciente["DiabetesPrediction"]==1 else "Não"))
print("Probabilidades de Diabetes: " + str(infoPaciente["Probability"]))