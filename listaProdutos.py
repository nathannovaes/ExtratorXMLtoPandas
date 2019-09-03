''''

b =('Teste','x','y')

a = []

a.append(b)

print(a)

c = ('z','a','b')

a.append(c)

print(a)

print(a[1][2])


'''
from escreveExcel import *
lista =[]
i = 0
j = 0
#Lista os produtos e guarda
def listaProdutos(data, nome, municipio, numNF, nat, natureza, fornecedor, cfop, pisconfins, vICMS, zero, vProd, Venc):
    b =(data, nome, municipio, numNF, nat, natureza, fornecedor, cfop, pisconfins, vICMS, zero, zero, vProd, vProd, zero, vProd, Venc)

    lista.append(b)



def mostraLista():
    # Tamanho da lista
    tamLista = len(lista)

    # Lanca na planilha a lista de produtos
    i = 0
    while i < tamLista:
        #            id, data,        nome,       municipio,   numNF,       nat,         natureza,    fornecedor,  cfop,        pisconfins,  vICMS,       v1,           v2,           vProd,        vProd2,       v3,           vProd3,       Venc
        lancaPlanilha(i, lista[i][0], lista[i][1],lista[i][2], lista[i][3], lista[i][4], lista[i][5], lista[i][6], lista[i][7], lista[i][8], lista[i][9], lista[i][10], lista[i][11], lista[i][12], lista[i][13], lista[i][14], lista[i][15], lista[i][16])
        i+=1

