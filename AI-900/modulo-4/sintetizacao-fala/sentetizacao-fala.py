import requests
from playsound import playsound
# python -m pip install playsound==1.2.2
from os import system, name, path
tracos = "=" * 40
# Preencher os dados
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Regiao da API
regiaoApi = "REGIAO_API"
# Header da requisição
cabecalho = { "Ocp-Apim-Subscription-Key" : chave, 
              "Content-Type" : "application/ssml+xml",
              "X-Microsoft-OutputFormat" : "audio-16khz-128kbitrate-mono-mp3" }
# Configurações de 
caminhoAtual = path.dirname(__file__)
arquivoDestino = caminhoAtual + "\\destino.mp3"
# Função para limpar a tela
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")
# Capturando o audio
clear()
# Capturando o audio
texto = input("Escreva o texto que deseja ser sintetizado.\n")
# Montagem do XML para envio
corpoRequisicao = f"""<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
<voice name="pt-BR-FranciscaNeural">
<prosody rate="-10%" pitch="5%">{texto}</prosody>
</voice>
</speak>"""
urlReq = f"https://{regiaoApi}.tts.speech.microsoft.com/cognitiveservices/v1"
# Efetuando a requisição para a Azure
res = requests.post(urlReq,data=corpoRequisicao, headers=cabecalho)
# Gravando a resposta da requisição
with open(arquivoDestino, 'wb') as fd:
  fd.write(res.content)
# Tocando o audio
playsound(arquivoDestino)