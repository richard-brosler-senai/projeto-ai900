import requests,json
from time import sleep
from click import clear
# Preencher os dados
# URL Ponto de extremidade para envio de Urls de imagens
urlApi = "URL_DA_API"
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Imagens para teste
imagens = [
    {
        "id" : 1,
        "titulo" : "Arduino",
        "url" : "https://www.robocore.net/upload/tutoriais/329_img_2_H.png?857"
    },
    {
        "id" : 2,
        "titulo" : "Raspberry",
        "url" : "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg/1200px-Raspberry_Pi_4_Model_B_-_Side.jpg"
    },
    {
        "id" : 3,
        "titulo" : "Cabos",
        "url" : "https://blog.plugmais.com.br/wp-content/uploads/2018/04/184755-conheca-as-principais-categorias-de-cabos-de-rede.jpg"
    },
    {
        "id" : 4,
        "titulo" : "Tanque",
        "url" : "https://a-static.mlcdn.com.br/1500x1500/tanque-de-guerra-de-metal-verde-militar-33cm-estilo-retro-verito/euqueroum/823/136bd3111a996ac0d045735259af8192.jpg"
    }
]
# Montando o cabeção de envio
cabecalhoEnvio = { "Content-Type" : "application/json", "Prediction-Key": chave }
# Realizando a requisição do serviço
# Limpando a tela
tracos = "=" * 40
clear()
for img in imagens: 
    # Texto para envio, alterar os dados para enviar
    print("Enviando uma imagem de",img.get("titulo",""))
    dadosEnvio = { "Url" : img["url"] }
    retorno = requests.post(urlApi, json=dadosEnvio, headers=cabecalhoEnvio)
    print(json.dumps(retorno.json(),indent=2))
    print(tracos)
    print("Predicções encontradas (Boxes Medidas: Esquerda,Topo,Comprimento, Altura):")
    for pred in retorno.json()["predictions"]:
        boxes = "Box:{left},{top},{width},{height})".format(**pred["boundingBox"])
        print("\t{tagName}({probability} - ".format(**pred) + boxes)
    # fechando o bloco com traços
    print(tracos)
    # Dando uma pausa de 2 segundos para não estourar as requisições
    sleep(2)