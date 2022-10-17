import requests
import time
import json
from os import system, name, path
tracos = "=" * 40
# Preencher os dados
# Chave Primária de autenticacao
chave = "CHAVE_API"
# URL Ponto de extremidade
urlApi = "URL_API"
# Header da requisição
cabecalho = { "Ocp-Apim-Subscription-Key" : chave, "Content-Type" : "application/json" }
# Configurações de 
caminhoAtual = path.dirname(__file__)
config = [
  {
    "id" : 1,
    "titulo" : "Avaliação 1 - The Royal Hotel, Londres, Reino Unido",
    "arquivo" : r"..\dados\review1.txt"
  },
  {
    "id" : 2,
    "titulo" : "Avaliação 2 - The Royal Hotel, Londres, Reino Unido",
    "arquivo" : r"..\dados\review2.txt"
  },
  {
    "id" : 3,
    "titulo" : "Avaliação 3 - The Lombard Hotel, São Francisco, EUA",
    "arquivo" : r"..\dados\review3.txt"
  },
  {
    "id" : 4,
    "titulo" : "Avaliação 4 - The Lombard Hotel, São Francisco, EUA",
    "arquivo" : r"..\dados\review4.txt"
  }
]
# Função para limpar a tela
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")
# Inicialização de variáveis
idTexto = 0
while (idTexto<1 or idTexto>4):
  clear()
  print("Para esse exemplo, escolha uma das opções de Avaliações abaixo:")
  for it in config:
    print("{id} - {titulo}".format(**it))
  try:
    idTexto = int(input("Digite uma das opções de avaliações:"))
  except:
    idTexto = 0
    print("Opção Inválida!")
    time.sleep(1)
itImg = config[idTexto - 1]
itCaminho = caminhoAtual + "\\"+ itImg["arquivo"]
print(f"\nVocê optou pela imagem {idTexto} que está em {itCaminho}")
contents = ""
with open(itCaminho, encoding='utf8') as f:
  contents = f.read()
print("conteúdo do texto:")
print(tracos)
print(contents)
print(tracos)
# Enviando para a Azure para fazer as avaliações
corpoRequisicao = { 
  "documents" : 
  [
    {
      "id" : 1,
      "text" : contents
    }
  ] 
}
# Fazendo a requisição para a Azure para obter a análise
print("*** Detectando Linguagem ***")
urlReq = urlApi + "/text/analytics/v3.1/languages"
res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
print(json.dumps(dadosRetorno,indent=2))
print(tracos)
for docResp in dadosRetorno["documents"]:
  lanDetect = docResp["detectedLanguage"]
  print("Linguagem: {name} ({iso6391Name}) - ({confidenceScore})".format(**lanDetect))
print(tracos)
# Procurando palavras chaves
print("*** Procurando palavras chaves ***")
urlReq = urlApi + "/text/analytics/v3.1/keyPhrases"
res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
print(json.dumps(dadosRetorno,indent=2))
print(tracos)
for docResp in dadosRetorno["documents"]:
  keyPhrases = docResp["keyPhrases"]
  print(f"Linguagem: {keyPhrases}")
print(tracos)
# Análise de Sentimentos
print("*** Análise de Sentimentos ***")
urlReq = urlApi + "/text/analytics/v3.1/sentiment"
res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
print(json.dumps(dadosRetorno,indent=2))
print(tracos)
for docResp in dadosRetorno["documents"]:
  sentimento = docResp["sentiment"]
  sentPos = docResp["confidenceScores"]["positive"]
  sentNeu = docResp["confidenceScores"]["neutral"]
  sentNeg = docResp["confidenceScores"]["negative"]
  print(f"Sentimento: {sentimento}")
  print("Scores:")
  print(f"  Positivo: {sentPos}")
  print(f"  Neutro: {sentNeu}")
  print(f"  Negativo: {sentNeg}")
  print("Analise dos sentimentos por Sentença do texto:")
  for sent in docResp["sentences"]:
    print("  Texto:{text}\n  Sentimento:{sentiment}".format(**sent))
    print("  Scores:")
    sentPos = sent["confidenceScores"]["positive"]
    sentNeu = sent["confidenceScores"]["neutral"]
    sentNeg = sent["confidenceScores"]["negative"]
    print(f"  Positivo: {sentPos}")
    print(f"  Neutro: {sentNeu}")
    print(f"  Negativo: {sentNeg}")
print(tracos)
# Identificando entidades conhecidas
print("*** Identificando entidades conhecidas ***")
urlReq = urlApi + "/text/analytics/v3.1/entities/linking"
res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
print(json.dumps(dadosRetorno,indent=2))
print(tracos)
for entidades in dadosRetorno["documents"]:
  for ent in entidades["entities"]:
    print("Nome: {name} - url: {url} fonte:{dataSource}".format(**ent))
