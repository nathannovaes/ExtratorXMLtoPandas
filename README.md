# ExtratorXML

Objetivo: Extrair da nota fiscal os dados que uma pessoa precisaria olhar e passar isso
para uma panilha em excel.

#Ferramentas:
- API ElementTree XML API

#Informações importantes:
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
