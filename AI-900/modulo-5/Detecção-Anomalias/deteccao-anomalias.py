import requests
# Função para texto na cor vermelha
def CorVermelha(texto):
    ret = f"\033[91m{texto}\033[00m"
    return ret
# Função para texto na cor verde
def CorVerde(texto):
    ret = f"\033[92m{texto}\033[00m"
    return ret
# Inicio do código
# Valores a serem preenchidos
end_point = "URL_API"
chave = "CHAVE_API"
# Inicio do programa
header = { "Ocp-Apim-Subscription-Key" : chave, "Content-Type" : "application/json" }
corpo = requests.get("https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/anomaly/data.json")
response = requests.post(end_point+"/anomalydetector/v1.0/timeseries/entire/detect",headers=header,json=corpo.json())
respData = response.json()
dadosEnv = corpo.json()
for itens in respData:
    if ( itens == "expectedValues" ):
        id = 0
        for it in respData[itens]:
            texto = dadosEnv["series"][id]["timestamp"] + " - " + str(dadosEnv["series"][id]["value"])
            textoAImprimir = CorVerde(texto) 
            if respData["isAnomaly"][id]:
                textoAImprimir = CorVermelha(texto)
            print(textoAImprimir)
            id += 1
