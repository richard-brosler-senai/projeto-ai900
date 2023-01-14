import requests
import time
import json
import tkinter as tk
from os import system, name
from PIL import Image
from io import BytesIO
# Preencher os dados
# Chave Primária de autenticacao
chave = "CHAVE_API"
# URL Ponto de extremidade
urlApi = "URL_API"
# Header da requisição
cabecalho = { "Ocp-Apim-Subscription-Key" : chave, "Content-Type" : "application/json" }
# Montando a janela de exibição
window = tk.Tk()
window.title("Análise de Imagens")
window.geometry('800x400')

l = tk.Label(window, text="Escolha as opções de análise abaixo disponíveis:",font=("Helvetica",10,"bold"))
l.grid(row=0, column=0, columnspan=5,sticky='w')
# Configuração de opções
confOpc = [
    {
        "id" : 1,
        "valor" : "Adult",
        "texto" : "Conteúdo Adulto"
    },
    {
        "id" : 2,
        "valor" : "Brands",
        "texto" : "Marcas na Imagem"
    },
    {
        "id" : 3,
        "valor" : "Categories",
        "texto" : "Categoriza Imagens"
    },
    {
        "id" : 4,
        "valor" : "Color",
        "texto" : "Cores predominantes"
    },
    {
        "id" : 5,
        "valor" : "Description",
        "texto" : "Descritivo da Imagem"
    },
    {
        "id" : 6,
        "valor" : "Faces",
        "texto" : "Rostos na Imagem"
    },
    {
        "id" : 7,
        "valor" : "ImageType",
        "texto" : "Tipo de Imagem"
    },
    {
        "id" : 8,
        "valor" : "Objects",
        "texto" : "Objetos na Imagem"
    },
    {
        "id" : 9,
        "valor" : "Tags",
        "texto" : "Tags da Imagem"
    }
]
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

opcs = []
valores = []
opcoes = ""
idImg = 0
pathImg = ""

def monta_valores():
    global opcoes
    valores.clear()
    for opc in opcs:
        if (opc.get()!=0):
            valores.append(confOpc[opc.get()-1]["valor"])
    opcoes = ','.join(valores)
linha=1
coluna=1
for it in confOpc:
    opc = tk.IntVar()
    opcs.append(opc)
    c = tk.Checkbutton(window,text=it["texto"],variable=opc,onvalue=it["id"], offvalue=0,command=monta_valores)
    c.grid(row=linha,column=coluna,sticky='w')
    coluna+=1
    if coluna>5:
        linha+=1
        coluna=1

linha+=1
l2 = tk.Label(window,text="Escolha qual imagem deseja análise:", font=("Helvetica",10,"bold"))
l2.grid(padx=5,row=linha, column=0, columnspan=5,pady=5,sticky='w')

def escolha_imagem():
    global idImg, pathImg
    idImg = config[opcRad.get()-1]["id"]
    pathImg = config[opcRad.get()-1]["caminhoImagem"]
    l3.config(text=config[opcRad.get()-1]["titulo"])

linha+=1
opcRad = tk.IntVar()
for it in config:
    c = tk.Radiobutton(window,text=it["titulo"],variable=opcRad,value=it["id"],command=escolha_imagem)
    c.grid(row=linha,column=0,columnspan=5,sticky='w')
    linha+=1

linha+=1
l3 = tk.Label(window, text="Imagem Escolhida foi:",font=("Helvetica",10,"bold"))
l3.grid(padx=5,row=linha, column=0, columnspan=5,sticky='w')

def mostrar_imagem():
    response = requests.get(pathImg)
    img = Image.open(BytesIO(response.content))
    img.show()

linha+=1
btn = tk.Button(window, text="Pressione para visualizar a imagem", command=mostrar_imagem)
btn.grid(padx=10, pady=10, row=linha,column=0,columnspan=5,sticky='w')

def analise_imagem():
    # Url de chamada da api
    urlReq = urlApi + "/vision/v3.2/analyze?visualFeatures=" + opcoes
    corpoRequisicao = { "url" : pathImg }
    # Fazendo a requisição para a Azure para obter a análise
    res = requests.post(urlReq,json=corpoRequisicao, headers=cabecalho)
    dadosRetorno = res.json()

linha+=1
btn = tk.Button(window, text="Pressione para analisar a imagem", command=analise_imagem)
btn.grid(padx=10, pady=10, row=linha,column=0,columnspan=5,sticky='w')

window.mainloop()

