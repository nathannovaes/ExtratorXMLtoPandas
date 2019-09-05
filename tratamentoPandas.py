import pandas as pd

def tratamentoPandas(lista):
       # Guarda a lista para ser tratada pelo Pandas
       lst = lista

       # Cria as colunas com base na lista
       df = pd.DataFrame(lst,
                         columns=['Data', 'Nome', 'Município', 'numNF', 'Natureza', 'Operação', 'Fornecedor', 'CFOP',
                                  'PIS/COFINS', 'vICMS', 'x', 'x', 'ValorA', 'x', 'ValorB', 'ValorC', 'Data Ven'])

       # Exibe a lista
       print(df)

       df_new = df.groupby(['Nome', 'numNF', 'Fornecedor', 'CFOP']).sum()


       print(df_new)
