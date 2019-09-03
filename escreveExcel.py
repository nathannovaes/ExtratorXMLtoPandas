import openpyxl

def lancaPlanilha(id, data,nome,municipio,numNF,nat,natureza,fornecedor,cfop,pisconfins,vICMS,v1,v2,vProd,vProd2,v3,vProd3,Venc):

    # Abre a opção para escrever um documento Excel
    arquivo=openpyxl.load_workbook("teste.xlsx")

    # Pega a aba que será utilizada do arquivo Excel
    w = arquivo.get_sheet_by_name('Sheet')

    # Ajuda a localizar qual linha serão gravado os dados
    end = str(id + 1)

    # Coloca os valores em cada célula do Excel
    w['A'+ end] = data
    w['B'+ end] = nome
    w['C'+ end] = municipio
    w['D'+ end] = numNF
    w['E'+ end] = nat
    w['F'+ end] = natureza
    w['G'+ end] = fornecedor
    w['H'+ end] = cfop
    w['I'+ end] = pisconfins
    w['J'+ end] = vICMS
    w['K'+ end] = v1
    w['L'+ end] = v2
    w['M'+ end] = vProd
    w['N'+ end] = vProd2
    w['O'+ end] = v3
    w['P'+ end] = vProd3
    w['Q'+ end] = Venc

    # Salva o arquivo
    arquivo.save("teste.xlsx")
