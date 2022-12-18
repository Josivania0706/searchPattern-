def searchPattern(pat, txt):
  #Armazenar as entradas
  texto = txt[0]
  padrao= pat[0]

  #Armazenar as posições (indexes) com o padrão reconhecido
  posPadrao = []
  posLeitura = []

  i = j = 0

  #O laço vai executar enquanto todo o texto não tiver sido lido completamente 
  while i < len(texto):                                                                     
    
    #Encontrei um caractere pertencente ao padrão
    if texto[i] == padrao[j]:  
      posPadrao.append(i) #Armazeno a posição deste caractere       
      posLeitura.append(i)

      #Padrão lido por inteiro
      if j == (len(padrao) - 1):
        #Imprimo posição 0, com o índice inicial do padrão
        print("Padrão encontrado no index  ",posPadrao[0])
        del posPadrao[:]  #Remove todos os índices armazenados do padrão
      i = posLeitura[0]
      del posLeitura[:]  #Remove todos os índices armazenados do padrão
      j = 0 #reseto o j para percorrer o padrão em outra iteração

      #Padrão não lido por inteiro, vou para próximo índice
      if j < (len(padrao) - 1):   
        j = j + 1
    
    else:#caractere diferente da sequência
      if j != 0: #a sequência do padrão foi quebrada
        i = i - 1 # a leitura deve continuar do caracter já lido
        i = posLeitura[0]
        del posLeitura[:]  #Remove todos os índices armazenados do padrão

      j = 0
      del posPadrao[:]  #Remove todos os índices armazenados
     
    i = i + 1 #Segue para próximo índice do texto


#Entrada com texto e o padrão procurado
#txt = ["CABBAA DCABBA DCABBAD"]  
#pat = ["ABBA"]                

#txt = ["Aqui tem um texto"]  
#pat = ["tem"]

txt = ["AAAABAAAAAAAAB"]  
pat = ["AAA"]

searchPattern(pat, txt)