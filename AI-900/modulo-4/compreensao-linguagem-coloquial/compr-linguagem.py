import requests
import json
from os import system, name, path
tracos = "=" * 40
# Preencher os dados
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Url da Api
urlApi = "URL_API"
# Nome do Projeto
projectName = "PROJECT_NAME"
# Nome do deploy
deployName = "DEPLOY_NAME"
# Header da requisição
cabecalho = { "Ocp-Apim-Subscription-Key" : chave, "Content-Type" : "application/json" }
# Função para limpar a tela
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")
# Digitando a ação para enviar ao projeto
print(tracos)
intencao = input("Entre com o texto para o envio:")
# Montagem do corpo de envio
corpoRequisicao = {
	"kind": "Conversation",
	"analysisInput": {
		"conversationItem": {
			"id": "1",
			"text": intencao,
			"participantId": "1"
		}
	},
	"parameters": {
		"projectName": projectName,
		"deploymentName": deployName,
		"stringIndexType": "TextElement_V8"
	}
}
# Fazendo a requisição para a Azure para obter a análise
urlReq = urlApi
res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
print(tracos)
print(json.dumps(dadosRetorno,indent=2))
print(tracos)
intencaoDetectada = dadosRetorno["result"]["prediction"]["topIntent"]
dispositivoDetectado = dadosRetorno["result"]["prediction"]["entities"][0]["text"]
print(f"Intenção detectada: {intencaoDetectada}")
print(f"Dispositivo detectado: {dispositivoDetectado}")
if (intencaoDetectada == "LigarDispositivo"):
  print(f"{dispositivoDetectado} foi ligado!")
elif (intencaoDetectada == "DesligarDispositivo"):
  print(f"{dispositivoDetectado} foi desligado!")
else:
  print("Não foi possível detectar a intenção!")
