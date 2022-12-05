from time import sleep
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
# python -m pip install scipy
# python -m pip install sounddevice
# python -m pip install playsound==1.2.2
import requests
import json
from os import system, name, path
tracos = "=" * 40
# Preencher os dados
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Regiao da API
regiaoApi = "REGIAO_API"
# Idiomas disponíveis para a nossa aplicação
config = [
  {
    "id" : 1,
    "sigla" : "en",
    "idioma" : "Inglês",
    "voz" : "en-US-JennyNeural"
  },
  {
    "id" : 2,
    "sigla" : "fr",
    "idioma" : "Francês",
    "voz" : "fr-FR-CelesteNeural"
  },
  {
    "id" : 3,
    "sigla" : "de",
    "idioma" : "Alemão",
    "voz" : "de-DE-KatjaNeural"
  },
  {
    "id" : 4,
    "sigla" : "ja",
    "idioma" : "Japonês",
    "voz" : "ja-JP-NanamiNeural"
  },
  {
    "id" : 5,
    "sigla" : "ko",
    "idioma" : "Coreano",
    "voz" : "ko-KR-InJoonNeural"
  },
  {
    "id" : 6,
    "sigla" : "ar",
    "idioma" : "Árabe",
    "voz" : "ar-QA-MoazNeural"
  },
]
# Header da requisição
cabecalho = { "Ocp-Apim-Subscription-Key" : chave, "Content-Type" : "audio/wav" }
# Configurações de 
caminhoAtual = path.dirname(__file__)
nomeArquivo = caminhoAtual + '\\output.wav'
arquivoDestino = caminhoAtual + "\\destino.mp3"
# rate do audio
fs = 44100
# Tempo do audio em segundos
seconds = 10
# Função para limpar a tela
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")
# Capturando o audio
clear()
print("Pense em uma frase que possa demorar %d segundos" % seconds)
print("Anote no papel e quando estiver pronto, tecle enter")
input()
# Realizando a gravação do audio para poder enviar
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Esperando até a gravação terminar
write(nomeArquivo, fs, myrecording) # Gravando o arquivo de saída de audio
# Preparando para enviar para a api da Azure
with open(nomeArquivo, 'rb') as f:
    corpoRequisicao = f.read()
urlReq = f"https://{regiaoApi}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=pt-BR"
res = requests.post(urlReq,data=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
print(tracos)
print(json.dumps(dadosRetorno,indent=2))
print(tracos)
textoFala = dadosRetorno["DisplayText"]
# Agora iremos enviar para a tradução em outros idiomas
idIdioma=0
while (idIdioma<1 or idIdioma>5):
  clear()
  print(f"Você disse: {textoFala}")
  print("Qual dos idiomas você deseja que seja traduzido? Veja as opções abaixo:")
  for idiom in config:
    print("{id} - {idioma} ({sigla})".format(**idiom))
  try:
    idIdioma = int(input("Digite o id do idioma desejado:"))
  except:
    idIdioma = 0
    print("Opção inválida!")
    sleep(1)
# Obtendo os dados do idioma desejado
itIdioma = config[idIdioma - 1]
idDest = itIdioma["sigla"]
vozTradutor = itIdioma["voz"]
# Preparando para o envio para ser traduzido
urlReq = f"https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=pt-br&to={idDest}&profanityAction=Marked"
# cabeçalho da requisição
cabecalho = { 
              "Ocp-Apim-Subscription-Key" : chave, 
              "Ocp-Apim-Subscription-Region" : regiaoApi,
              "Content-Type" : "application/json" 
            }
# corpo da requisição
corpoRequisicao = [{ "text" : textoFala }]
# Enviando para tradução
res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
dadosRetorno = res.json()
print(tracos)
print(json.dumps(dadosRetorno,indent=2))
print(tracos)
traducao = dadosRetorno[0]["translations"][0]["text"]
print(f"O texto traduzido foi: {traducao}")
# Passando a tradução para fala
print(tracos)
print("Agora vamos passar para fala o que foi traduzido.")
corpoRequisicao = f"""<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
<voice name="{vozTradutor}">
<prosody rate="0%" pitch="0%">{traducao}</prosody>
</voice>
</speak>"""
urlReq = f"https://{regiaoApi}.tts.speech.microsoft.com/cognitiveservices/v1"
# Efetuando a requisição para a Azure
cabecalho = { "Ocp-Apim-Subscription-Key" : chave, 
              "Content-Type" : "application/ssml+xml; charset=UTF-8",
              "X-Microsoft-OutputFormat" : "audio-16khz-128kbitrate-mono-mp3" }
res = requests.post(urlReq,data=corpoRequisicao.encode("utf-8"), headers=cabecalho)
# Gravando a resposta da requisição
with open(arquivoDestino, 'wb') as fd:
  fd.write(res.content)
# Tocando o audio
playsound(arquivoDestino)