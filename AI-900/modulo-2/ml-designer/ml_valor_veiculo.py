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
                     "symboling": 3,                # Simbolizando
                     "normalized-losses": 1.0,      # Perdas normalizadas
                     "make": "alfa-romero",         # Marca
                     "fuel-type": "gas",            # Tipo de Combustível
                     "aspiration": "std",           # Aspiração
                     "num-of-doors": "two",         # Número de portas
                     "body-style": "convertible",   # Estilo do Corpo
                     "drive-wheels": "rwd",         # Rodas Motrizes
                     "engine-location": "front",    # Localização do Motor
                     "wheel-base": 88.6,            # Distância entre Eixos
                     "length": 168.8,               # Comprimento
                     "width": 64.1,                 # Largura
                     "height": 48.8,                # Altura
                     "curb-weight": 2548,           # Peso do freio
                     "engine-type": "dohc",         # Tipo do Motor
                     "num-of-cylinders": "four",    # Número de cilindros
                     "engine-size": 130,            # Tamanho do Motor
                     "fuel-system": "mpfi",         # Sistema de Combustível
                     "bore": 3.47,                  # Calibre
                     "stroke": 2.68,                # Pressão Cilindros
                     "compression-ratio": 9,        # Taxa de compressão
                     "horsepower": 111,             # Potência em cavalos de força
                     "peak-rpm": 5000,              # RPM 
                     "city-mpg": 21,                # Consumo na cidade em milhas por galão
                     "highway-mpg": 27              # Consumo na rodovia em milhas por galão
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