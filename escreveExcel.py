from openpyxl import Workbook

def lancaPlanilha(data, nome, municipio, numNF, natureza, fornecedor, cfop, pisconfins, vICMS, vProd, Venc):
    wb = Workbook()

    # grab the active worksheet
    w = wb.active

    # Data can be assigned directly to cells
    w['A1'] = data
    w['B1'] = nome
    w['C1'] = municipio
    w['D1'] = numNF
    w['E1'] = 'Devolução'
    w['F1'] = natureza
    w['G1'] = fornecedor
    w['H1'] = cfop
    w['I1'] = pisconfins
    w['J1'] = vICMS
    w['K1'] = '0'
    w['L1'] = '0'
    w['M1'] = vProd
    w['N1'] = vProd
    w['O1'] = '0'
    w['P1'] = vProd
    w['Q1'] = Venc

    # Rows can also be appended
    #ws.append([1, 2, 3])


    # Save the file
    wb.save("teste.xlsx")