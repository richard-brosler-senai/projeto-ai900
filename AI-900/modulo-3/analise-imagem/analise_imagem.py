import requests
import time
# Preencher os dados
# Chave Primária de autenticacao
chave = "8bc6cb095db644b797762fb730dd9bd1"
# URL Ponto de extremidade
urlApi = "https://brosler-visual.cognitiveservices.azure.com/"
# Header da requisição
cabecalho = { "Ocp-Apim-Subscription-Key" : chave, "Content-Type" : "application/json" }
# Opções de análise ativadas
# URL da documentação da Api https://westus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/56f91f2e778daf14a499f21b
# Adult - Verifica se há conteúdo adulto ou violência
# Brands - Verifica existência de marcas
# Categories - Categoriza as imagens
# Color - Determina as cores dominantes
# Description - Descreve o conteúdo da imagem
# Faces - Determina se há rostos na imagem e onde estão localizadas
# ImageType - Determina se a imagem é um clipart ou um desenho livre
# Objects - Detecta os objetos na imagem
# Tags - Relaciona as tags da imagem
opcoes = "Adult,Brands,Categories,Color,Description,Faces,ImageType,Objects,Tags"
# Configuração das imagens
config = [
  {
    "id" : 1,
    "caminhoImagem" : "https://learn.microsoft.com/pt-br/training/wwl-data-ai/analyze-images-computer-vision/media/store-camera-1.jpg"
  },
  {
    "id" : 2,
    "caminhoImagem" : "https://learn.microsoft.com/pt-br/training/wwl-data-ai/analyze-images-computer-vision/media/store-camera-2.jpg"
  },
  {
    "id" : 3,
    "caminhoImagem" : "https://learn.microsoft.com/pt-br/training/wwl-data-ai/analyze-images-computer-vision/media/store-camera-3.jpg"
  },
  {
    "id" : 4,
    "caminhoImagem" : "https://s2.glbimg.com/rrSKiwOqeWMO978oP56iew3R8Rc=/0x0:3910x2719/924x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_da025474c0c44edd99332dddb09cabe8/internal_photos/bs/2022/k/X/KWfdIoRkeVsZfKUOa4aA/389975108-1-.jpg"
  }
]
# Url de chamada da api
urlReq = urlApi + "/vision/v3.2/analyze?visualFeatures=" + opcoes
# Inicialização de variáveis
limpaTela = chr(27) + "[2J"
idImagem = 0
while (idImagem<1 or idImagem>4):
  print(limpaTela)
  print("Para esse exemplo, escolha uma das opções de imagem abaixo:")
  for it in config:
    print(it["id"])
  try:
    idImagem = int(input("Digite uma das opções de imagem:"))
  except:
    idImagem = 0
    print("Opção Inválida!")
    time.sleep(1)
itImg = config[idImagem - 1]
itCaminho = itImg["caminhoImagem"]
print(f"Você optou pela imagem {idImagem} que está em {itCaminho}")
print("Iniciando o processo de Análise de imagem...")

corpoRequisicao = { "url" : itCaminho }
res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
# Mostrando os resultados
print("Verificando se há conteúdo adulto, racismo ou sangrento...")
#Dados sobre Adulto, racismo ou sangrento
adulto = "Sim" if dadosRetorno["adult"]["isAdultContent"] else "Não"
adultoPerc = dadosRetorno["adult"]["adultScore"]
racismo = "Sim" if dadosRetorno["adult"]["isRacyContent"] else "Não"
racismoPerc = dadosRetorno["adult"]["racyScore"]
sangrento = "Sim" if dadosRetorno["adult"]["isGoryContent"] else "Não"
sangrentoPerc = dadosRetorno["adult"]["goreScore"]
print(f"Conteúdo tem adulto? {adulto} - score: {adultoPerc}")
print(f"Conteúdo tem racismo? {racismo} - score: {racismoPerc}")
print(f"Conteúdo tem sangue? {sangrento} - score: {sangrentoPerc}")
# Verificando se tem marcas
print("Verificando se há marcas, se tiver, mostraremos")
for marcas in dadosRetorno["brands"]:
  mq = marcas["name"]
  mqperc = marcas["confidence"]
  posximg = marcas["rectangle"]["x"]
  posyimg = marcas["rectangle"]["y"]
  poswimg = marcas["rectangle"]["w"]
  poshimg = marcas["rectangle"]["h"]
  print(f"Nome da marca: {mq} - % de confiança: {mqperc} - posicionamento x: {posximg} y:{posyimg} larg: {poshimg} compr: {poswimg}")