import requests
import time
import json
tracos = "========================================="
# Preencher os dados
# Chave Primária de autenticacao
chave = "CHAVE_API"
# URL Ponto de extremidade
urlApi = "URL_API"
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
    "titulo" : "Mulher com Criança no supermercado",
    "caminhoImagem" : "https://learn.microsoft.com/pt-br/training/wwl-data-ai/analyze-images-computer-vision/media/store-camera-1.jpg"
  },
  {
    "id" : 2,
    "titulo" : "Mulher fazendo compras no supermercado",
    "caminhoImagem" : "https://learn.microsoft.com/pt-br/training/wwl-data-ai/analyze-images-computer-vision/media/store-camera-2.jpg"
  },
  {
    "id" : 3,
    "titulo" : "Mulher Oriental no supermercado",
    "caminhoImagem" : "https://learn.microsoft.com/pt-br/training/wwl-data-ai/analyze-images-computer-vision/media/store-camera-3.jpg"
  },
  {
    "id" : 4,
    "titulo" : "Mulher saindo de uma AppleStore",
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
    print("{id} - {titulo}".format(**it))
  try:
    idImagem = int(input("Digite uma das opções de imagem:"))
  except:
    idImagem = 0
    print("Opção Inválida!")
    time.sleep(1)
itImg = config[idImagem - 1]
itCaminho = itImg["caminhoImagem"]
print(f"\nVocê optou pela imagem {idImagem} que está em {itCaminho}")
# Iniciando as verificações e requisição para a Azure
print(tracos)
print("Mostrando o retorno da API")
corpoRequisicao = { "url" : itCaminho }
# Fazendo a requisição para a Azure para obter a análise
res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
# Mostrando o JSON de retorno
print(json.dumps(dadosRetorno,indent=3))
print(tracos)
print("Iniciando o processo de Análise de imagem...")
# Mostrando os resultados
if (not(dadosRetorno.get("adult") is None)):
  print("Verificando se há conteúdo adulto, racismo ou sangrento...")
  #Dados sobre Adulto, racismo ou sangrento
  adulto = "Sim" if dadosRetorno["adult"]["isAdultContent"] else "Não"
  adultoPerc = dadosRetorno["adult"]["adultScore"]
  racismo = "Sim" if dadosRetorno["adult"]["isRacyContent"] else "Não"
  racismoPerc = dadosRetorno["adult"]["racyScore"]
  sangrento = "Sim" if dadosRetorno["adult"]["isGoryContent"] else "Não"
  sangrentoPerc = dadosRetorno["adult"]["goreScore"]
  print(f"\tConteúdo tem adulto? {adulto} - score: {adultoPerc}")
  print(f"\tConteúdo tem racismo? {racismo} - score: {racismoPerc}")
  print(f"\tConteúdo tem sangue? {sangrento} - score: {sangrentoPerc}")
# Verificando se tem marcas
if (not(dadosRetorno.get("brands") is None)):
  print(tracos)
  print("Verificando se há marcas, se tiver, mostraremos")
  for marcas in dadosRetorno["brands"]:
    mq = marcas["name"]
    mqperc = marcas["confidence"]
    posximg = marcas["rectangle"]["x"]
    posyimg = marcas["rectangle"]["y"]
    poswimg = marcas["rectangle"]["w"]
    poshimg = marcas["rectangle"]["h"]
    print(f"\tNome da marca: {mq} ({mqperc}) - Localização Esq.: {posximg} Topo:{posyimg} larg: {poshimg} compr: {poswimg}")
# Verificando as cores predominantes na imagem
if (not(dadosRetorno.get("color") is None)):
  print(tracos)
  print("Verificando as cores predominantes na imagem")
  print("\tCor fundo predominante é %s" % (dadosRetorno["color"]["dominantColorBackground"]))
  print("\tCor predominante é %s." % (dadosRetorno["color"]["dominantColorForeground"]))
# Verificando o tipo de imagem
if (not(dadosRetorno.get("imageType") is None)):
  print(tracos)
  print("Verificando o tipo de imagem")
  print("\tA imagem é ClipArt? Se for, o tipo é %d" % (dadosRetorno["imageType"]["clipArtType"]))
  print("\tA imagem é um desenho livre (traços)? Se for, o tipo é %d" % (dadosRetorno["imageType"]["lineDrawingType"]))
# Verificando as tags
if (not(dadosRetorno.get("tags") is None)):
  print(tracos)
  print("Verificando tags sobre a imagem")
  print("\tTag ( Confiabilidade )")
  for tags in dadosRetorno["tags"]:
    print("\t{name} ({confidence})".format(**tags))
# Descrevendo a imagem
if (not(dadosRetorno.get("description") is None)):
  print(tracos)
  print("Descrevendo o conteúdo da imagem")
  print("tags da descrição constantes:")
  desTags = ""
  separador = ""
  for tags in dadosRetorno["description"]["tags"]:
    desTags += separador + tags
    separador = ", "
  print(f"\t{desTags}")
  print("Descrições da imagem:")
  for descricoes in dadosRetorno["description"]["captions"]:
    print("\tDescritivo: {text}({confidence})".format(**descricoes))
# Faces na imagem
if (not(dadosRetorno.get("faces") is None)):
  print(tracos)
  print("Verificando a existência de faces na imagem, se tiver, mostraremos")
  for faces in dadosRetorno["faces"]:
    faceCoord = "Esquerda={left}, Topo={top}, Comp.={width}, Altura={height}".format(**faces["faceRectangle"])
    if (not (faces.get("age") is None)):
      print("\tIdade:{age} - gênero: {gender} - Localização do rosto:".format(**faces) + faceCoord)
    else:
      print("\tLocalização do rosto:".format(**faces) + faceCoord)
# Objetos na imagem
if (not(dadosRetorno.get("objects") is None)):
  print(tracos)
  print("Verificando a existência de objetos na imagem, se tiver, mostraremos")
  for objetos in dadosRetorno["objects"]:
    objCoord = "Esquerda={x}, Topo={y}, Comp.={w}, Altura={h}".format(**objetos["rectangle"])
    print("\tObjeto:{object}({confidence}) - Localização do objeto:".format(**objetos) + objCoord)
