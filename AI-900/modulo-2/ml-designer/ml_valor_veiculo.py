import json
import requests
# Preencher os dados
# URL Ponto de extremidade
urlApi="URL_API"
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Texto para envio, alterar os dados para enviar
dadosEnvio = {
 "Inputs": {
             "WebServiceInput0":
             [
                 {
                     "symboling": 3,                # Simbolizando (valores de -3 a 3)
                     "normalized-losses": 1.0,      # Perdas normalizadas ( valores entre 65 e 256)
                     "make": "alfa-romero",         # Marca (disponíveis alfa-romero, audi, bmw, chevrolet, dodge, honda, isuzu, jaguar, mazda, mercedes-benz, mercury, mitsubishi, nissan, peugot, plymouth, porsche, renault, saab, subaru, toyota, volkswagen, volvo)
                     "fuel-type": "gas",            # Tipo de Combustível (disponíveis diesel, gas)
                     "aspiration": "std",           # Aspiração (disponíveis std, turbo)
                     "num-of-doors": "two",         # Número de portas (disponíveis four, two)
                     "body-style": "convertible",   # Estilo do Corpo (disponíveis hardtop, wagon, sedan, hatchback, convertible)
                     "drive-wheels": "rwd",         # Rodas Motrizes (disponíveis 4wd, fwd, rwd)
                     "engine-location": "front",    # Localização do Motor (disponíveis front, rear)
                     "wheel-base": 88.6,            # Distância entre Eixos (valores entre 86.6 e 120.9)
                     "length": 168.8,               # Comprimento (valores entre 141.1 e 208.1)
                     "width": 64.1,                 # Largura (valores entre 60.3 e 72.3)
                     "height": 48.8,                # Altura (valores entre 47.8 e 59.8)
                     "curb-weight": 2548,           # Peso do freio (valores entre 1488 e 4066)
                     "engine-type": "dohc",         # Tipo do Motor (disponíveis dohc, dohcv, l, ohc, ohcf, ohcv, rotor)
                     "num-of-cylinders": "four",    # Número de cilindros (disponíveis eight, five, four, six, three, twelve, two)
                     "engine-size": 130,            # Tamanho do Motor (valores entre 61 e 326)
                     "fuel-system": "mpfi",         # Sistema de Combustível (disponíveis 1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi, spfi)
                     "bore": 3.47,                  # Calibre (valores entre 2.54 e 3.94)
                     "stroke": 2.68,                # Pressão Cilindros (valores entre 2.07 e 4.17)
                     "compression-ratio": 9,        # Taxa de compressão (valores entre 7 to 23)
                     "horsepower": 111,             # Potência em cavalos de força (valores entre 48 e 288)
                     "peak-rpm": 5000,              # RPM (valores entre 4150 e 6600)
                     "city-mpg": 21,                # Consumo na cidade em milhas por galão (valores entre 13 e 49)
                     "highway-mpg": 27              # Consumo na rodovia em milhas por galão (valores entre 16 e 54)
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
print("----------------------------------")
print(json.dumps(retorno.json(),indent=3))