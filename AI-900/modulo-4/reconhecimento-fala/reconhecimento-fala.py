import sounddevice as sd
from scipy.io.wavfile import write
# python -m pip install scipy
# python -m pip install sounddevice
import requests
import json
from os import system, name, path
tracos = "=" * 40
# Preencher os dados
# Chave Primária de autenticacao
chave = "CHAVE_API"
# Regiao da API
regiaoApi = "REGIAO_API"
# Header da requisição
cabecalho = { "Ocp-Apim-Subscription-Key" : chave, "Content-Type" : "audio/wav" }
# Configurações de 
caminhoAtual = path.dirname(__file__)
nomeArquivo = caminhoAtual + '\\output.wav'
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
print("Você disse: {DisplayText}".format(**dadosRetorno))
