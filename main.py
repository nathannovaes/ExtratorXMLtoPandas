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
#Seleciona o arquivo que vamos manipular
tree = ET.parse('1.xml')
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
print(root[0][0][1][2][4].text)

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
    #Código fiscal de operação
    print(root[0][0][i][0][5].text)
    #Valor total
    print(root[0][0][i][0][9].text)
    #Valor ICMS
    #Faz uma validação para ver se o produto tem imposto. Se for CFOP 5202, ele tem.
    if root[0][0][i][0][5].text == '5202':
        print(root[0][0][i][1][0][0][5].text)
    else:
        print('0')
    i+=1

####VENCIMENTO
#Somamos + 2 em i, porque assim pulamos direto para a tag da cobrança cobr.
i += 2
print(root[0][0][i][1][1].text)


