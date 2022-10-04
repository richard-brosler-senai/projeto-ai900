import requests
# Preencher os dados
# URL Ponto de extremidade
urlApi="http://0dc68833-d88e-4f82-8c51-2f67a44912d9.brazilsouth.azurecontainer.io/score"
# Chave Primária de autenticacao
chave = "Xg1C12e0p6x2FgZqEhTDnPFCWtuNJPrw"
# Texto para envio, alterar os dados para enviar
dadosEnvio = {
 "Inputs": {
             "WebServiceInput0":
             [
                 {
                     "symboling": 3,
                     "normalized-losses": 1.0,
                     "make": "alfa-romero",
                     "fuel-type": "gas",
                     "aspiration": "std",
                     "num-of-doors": "two",
                     "body-style": "convertible",
                     "drive-wheels": "rwd",
                     "engine-location": "front",
                     "wheel-base": 88.6,
                     "length": 168.8,
                     "width": 64.1,
                     "height": 48.8,
                     "curb-weight": 2548,
                     "engine-type": "dohc",
                     "num-of-cylinders": "four",
                     "engine-size": 130,
                     "fuel-system": "mpfi",
                     "bore": 3.47,
                     "stroke": 2.68,
                     "compression-ratio": 9,
                     "horsepower": 111,
                     "peak-rpm": 5000,
                     "city-mpg": 21,
                     "highway-mpg": 27
                 }
             ]
         },
 "GlobalParameters": {}
 }
# Montando o cabeção de envio
cabecalhoEnvio = { "Content-Type" : "application/json", "Authorization": f"Bearer {chave}" }
# Realizando a requisição do serviço
retorno = requests.post(urlApi, json=dadosEnvio, headers=cabecalhoEnvio)
# Limpando a tela
print(chr(27) + "[2J") 
# Imprimindo o resultado
print("Preço do veículo previsto: " + str(retorno.json()["Results"]["WebServiceOutput0"][0]["predicted_price"]))