from time import sleep
import requests
import json
# Preencher os dados
# URL Ponto de extremidade para envio de Urls de imagens
urlApi = "URL_DA_API"
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Imagens para teste
imagens = [
    {
        "id" : 1,
        "titulo" : "Rottweiler",
        "url" : "https://www.petz.com.br/blog/wp-content/uploads/2021/11/rottweiler-e-bravo-3-1280x720.jpg"
    },
    {
        "id" : 2,
        "titulo" : "Pinscher",
        "url" : "https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia11196/pinscher-cursos-cpt.jpg"
    },
    {
        "id" : 3,
        "titulo" : "Donskoy",
        "url" : "https://allaboutcats.com/wp-content/uploads/2020/10/donskoy-compressed.jpg"
    },
    {
        "id" : 4,
        "titulo" : "Siamês",
        "url" : "https://blog.dramei.com.br/wp-content/uploads/2019/05/Gato-Siames2.jpg"
    },
    {
        "id" : 5,
        "titulo" : "Girafa",
        "url" : "https://i.pinimg.com/originals/dd/dd/0e/dddd0e2e49d03e9499847848f9b6a21d.jpg"
    }
]
# Montando o cabeção de envio
cabecalhoEnvio = { "Content-Type" : "application/json", "Prediction-Key": chave }
# Realizando a requisição do serviço
# Limpando a tela
tracos = "==================================="
print(chr(27) + "[2J") 
for img in imagens: 
    # Texto para envio, alterar os dados para enviar
    print("Enviando uma imagem de {titulo}".format(**img))
    dadosEnvio = { "Url" : img["url"] }
    retorno = requests.post(urlApi, json=dadosEnvio, headers=cabecalhoEnvio)
    print(json.dumps(retorno.json(),indent=2))
    print(tracos)
    print("Predicções encontradas:")
    for pred in retorno.json()["predictions"]:
        print("\t{tagName}({probability})".format(**pred))
    # fechando o bloco com traços
    print(tracos)
    # Dando uma pausa de 2 segundos para não estourar as requisições
    sleep(2)
