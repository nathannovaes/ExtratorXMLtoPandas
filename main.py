"""
DOCUMENTAÇÃO DO CÓDIGO

Objetivo: Extrair da nota fiscal os dados que uma pessoa precisaria olhar e passar isso
para uma panilha em excel.

Ferramentas:
- API ElementTree XML API

Informações importantes:
- A variável root corresponde ao nó principal da nossa árvore. Na Figura A o nosso
root seria a tag nfeProc.
- Para pegar uma informação de alguma tag, preocisamos acessar o nó correto. Para isso
é necessário especificar o caminho que vamos seguir. Por exemplo: root[a][b][c][n].text
Legenda: a = posição do primeiro nó, b = posição do segundo nó e assim respectivamente
Cada nó é identificado por um número. Na Figura A o nó root[0][0][1].text seria a tag
emit.

----------Figura A----------
<nfeProc versao="4.00">
   <NFe>
      <infNFe versao="4.00">
         <ide>
            Outros nós...
         </ide>
         <emit>
            Outros nós...
         </emit>
         <dest>
            Outros nós...
         </dest>
      </infNFe>
   </NFe
</nfeProc>
--------------------------



"""
####API
#Importa a API para manipular o XML
import xml.etree.ElementTree as ET
from fornecedor import *
from escreveExcel import *
from verificaPisConfins import *
from listaProdutos import *

#Seleciona o arquivo que vamos manipular
tree = ET.parse('3.xml')
#Guarda o aquivo dentro de root
root = tree.getroot()

####DATA
#Guarda o valor da data em uma variavel
data = root[0][0][0][6].text
#Exibe o valor em pedaço, pois só queremos a data. Não horas, minutos, segundos e etc.
data = data[:10]
print(data)

####NOME DO CLIENTE
nome = root[0][0][1][1].text
print(nome)

####MUNICÍPIO
#Foi necessário utilizar um Try/Except, pois nem toda nota possui o mesmo layout.
try:
    municipio = root[0][0][1][2][4].text
    print(municipio)
except:
    municipio = root[0][0][1][3][4].text
    print(municipio)


####NÚMERO FISCAL
numNF = root[0][0][0][5].text
print(numNF)

####NATUREZA DA OPERAÇÃO
natureza = root[0][0][0][2].text
print(natureza)


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
        cfop = root[0][0][i][0][5].text
        print(cfop)
    #Caso não encontre, o programa procura pega tag CFOP
    else:
        j = 1
        while root[0][0][i][0][j].tag != 'CFOP':
            j+=1
        cfop = root[0][0][i][0][j].text
        print(cfop)


    #Pis Confins
    #Identifica se o pis/confins é normal ou isento
    pisconfins = verificaPisConfis(fornecedor)

    #Valor total
    #Verifica se a tag é vProd
    if root[0][0][i][0][9].tag == 'vProd':
        vProd = root[0][0][i][0][9].text
        print(vProd)
    #Caso não encontre, o programa procura pega tag vProd
    else:
        j = 1
        while root[0][0][i][0][j].tag != 'vProd':
            j+=1
        vProd = root[0][0][i][0][j].text
        print(vProd)

    #Valor ICMS
    #Faz uma validação para ver se o produto tem imposto. Se for CFOP 5202, ele tem.

    if root[0][0][i][0][5].text == '5202':
        #Procura a tag ICMS
        j = 0
        while root[0][0][i][1][j].tag != 'ICMS':
            j += 1
        #Encontrou a tag ICMS
        #Procura pela tag vICMS
        k = 0
        while root[0][0][i][1][j][0][k].tag != 'vICMS':
            k += 1
        #Exibe o valor do imposto
        vICMS = root[0][0][i][1][j][0][k].text
        print(vICMS)
    else:
        vICMS = 0
        print(vICMS)
    listaProdutos(data, nome, municipio, numNF, 'Devolução', natureza, fornecedor, cfop, pisconfins, vICMS, '0',vProd)
    i+=1


####VENCIMENTO
#Somamos + 2 em i, porque assim pulamos direto para a tag da cobrança cobr.
i += 2
try:
    j = 0
    while root[0][0][i][1][j].tag != 'dVenc':
        j += 1
    Venc = root[0][0][i][1][j].text
    print(Venc)
except:
    #Se a nota não tem data de validade para pagamento, é necessário colocar.
    ano = data[0:5]
    mes = data[5:7]
    dia = data[7:10]
    numMes = int(mes) + 1
    mes = str(numMes)
    Venc = ano + mes + dia
    print(Venc)


#lancaPlanilha(data, nome, municipio, numNF, natureza, fornecedor, cfop, pisconfins, vICMS, vProd, Venc)
mostraLista(Venc)
