####API
#Importa a API para manipular o XML
import xml.etree.ElementTree as ET
from fornecedor import *

#Seleciona o arquivo que vamos manipular
tree = ET.parse('3.xml')
#Guarda o aquivo dentro de root
root = tree.getroot()

####DATA
#Guarda o valor da data em uma variavel
data = root[0][0][0][6].text
#Exibe o valor em pedaço, pois só queremos a data. Não horas, minutos, segundos e etc.
print(data[:10])

####NOME DO CLIENTE
print(root[0][0][1][1].text)

####CIDADE
#Foi necessário utilizar um Try/Except, pois nem toda nota possui o mesmo layout.
try:
  print(root[0][0][1][2][4].text)
except:
  print(root[0][0][1][3][4].text)


####NÚMERO FISCAL
print(root[0][0][0][5].text)

####NATUREZA DA OPERAÇÃO
print(root[0][0][0][2].text)


###DADOS DO PRODUTO
"""
Como de uma nota final para outra varia questão da quantidade de tags det, vamos usar
um loop para encontrar todos os produtos. O código abaixo pega o valor da posição da
tag det e pergunta: Ainda é det essa tag? Se sim, imprima os valores e ao final passe
para a próxima tag. Isso vai acontecer até que tenham acabado todas as tags det.
"""
i = 3
while root[0][0][i].tag == 'det':
    #Nome do produto
    print(root[0][0][i][0][2].text)
    fornecedor = encontraFornecedor(root[0][0][i][0][2].text)
    print(fornecedor)
    #Código fiscal de operação

    #Verifica se a tag é CFOP
    if root[0][0][i][0][5].tag == 'CFOP':
        print(root[0][0][i][0][5].text)
    #Caso não encontre, o programa procura pega tag CFOP
    else:
        j = 1
        while root[0][0][i][0][j].tag != 'CFOP':
            j+=1
        print(root[0][0][i][0][j].text)

    #Valor total
    #Verifica se a tag é vProd
    if root[0][0][i][0][9].tag == 'vProd':
        print(root[0][0][i][0][9].text)
    #Caso não encontre, o programa procura pega tag vProd
    else:
        j = 1
        while root[0][0][i][0][j].tag != 'vProd':
            j+=1
        print(root[0][0][i][0][j].text)

    #Valor ICMS
    #Faz uma validação para ver se o produto tem imposto. Se for CFOP 5202, ele tem.
    if root[0][0][i][0][5].text == '5202':
        #Procura a tag ICMS
        j = 1
        while root[0][0][i][1][j].tag != 'ICMS':
            j += 1
        #Encontrou a tag ICMS
        #Procura pela tag vICMS
        k = 1
        while root[0][0][i][1][j][0][k].tag != 'vICMS':
            k += 1
        #Exibe o valor do imposto
        print(root[0][0][i][1][j][0][k].text)
    else:
        print('0')
    i+=1

####VENCIMENTO
#Somamos + 2 em i, porque assim pulamos direto para a tag da cobrança cobr.
try:
    i += 2
    print(root[0][0][i][1][1].text)
except:
    #Se a nota não tem data de validade para pagamento, é necessário colocar.
    ano = data[0:5]
    mes = data[5:7]
    dia = data[7:10]
    numMes = int(mes) + 1
    mes = str(numMes)
    print(ano + mes + dia)

