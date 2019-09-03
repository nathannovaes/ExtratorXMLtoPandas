
#Verifica Pis e Confis, se é Normal ou Isento
def verificaPisConfis(fornecedor):
    if fornecedor == 'Agroinca':
        return 'Normal'
    elif fornecedor == 'Arbor':
        return 'Isento'
    elif fornecedor == 'Barilla':
        return 'Normal'
    elif fornecedor == 'Bonafont':
        return 'Isento'
    elif fornecedor == 'Casa Madeira':
        return 'Normal'
    elif fornecedor == 'Cerpa':
        return 'Isento'
    elif fornecedor == 'DGoias':
        return 'Normal'
    elif fornecedor == 'Goes':
        return 'Normal'
    elif fornecedor == 'Hemmer':
        return 'Normal'
    elif fornecedor == 'Juxx':
        return 'Normal'
    elif fornecedor == 'Kelco':
        return 'Normal'
    elif fornecedor == 'Mastig':
        return 'Normal'
    elif fornecedor == 'Nestle':
        return 'Isento'
    elif fornecedor == 'Nutry':
        return 'Normal'
    elif fornecedor == 'Prata':
        return 'Isento'
    elif fornecedor == 'Rio':
        return 'Normal'
    elif fornecedor == 'Socorro':
        return 'Isento'
    elif fornecedor == 'Tradipet':
        return 'Normal'
    elif fornecedor == 'CYT':
        return 'Isento'
    else:
        return 'Sem conhecimento'