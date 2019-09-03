
#Verifica o fornecedor
def encontraFornecedor(produto):

  if produto.find('AGROINCA') != -1:
      return 'Agroinca'
  elif produto.find('THEREZOPOLIS') != -1 or produto.find('AMERICANA') != -1:
      return 'Arbor'
  elif produto.find('BARILLA') != -1:
      return 'Barilla'
  elif produto.find('BONAFONT') != -1:
      return 'Bonafont'
  elif produto.find('CASA MADEIRA') != -1:
      return 'Casa Madeira'
  elif produto.find('CERPA') != -1:
      return 'Cerpa'
  elif produto.find('DGOIAS') != -1:
      return 'DGoias'
  elif produto.find('GOES') != -1:
      return 'Goes'
  elif produto.find('HEMMER') != -1:
      return 'Hemmer'
  elif produto.find('JUXX') != -1:
      return 'Juxx'
  elif produto.find('KELCO') != -1 or produto.find('PIPICAT') != -1:
      return 'Kelco'
  elif produto.find('MASTIG') != -1:
      return 'Mastig'
  elif produto.find('NESTLE') != -1 or produto.find('LOURENCO') != -1 or produto.find('PERRIER') != -1:
      return 'Nestle'
  elif produto.find('Nutry') != -1:
      return 'Nutry'
  elif produto.find('PRATA') != -1:
      return 'Prata'
  elif produto.find('RIO') != -1:
      return 'Rio'
  elif produto.find('ACQUISSIMA') != -1:
      return 'Socorro'
  elif produto.find('TRADIPET') != -1:
      return 'Tradipet'
  elif produto.find('CONCHA') != -1:
      return 'CYT'
  else:
      return 'Sem conhecimento'


