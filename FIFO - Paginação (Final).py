# encoding: iso-8859-1

import time

cont = 0
contHit = 0
contMiss = 0
frames = []

ref = raw_input("Digite a string de refer�ncias separadas por espa�o: ")
references = ref.split(" ")

#Inser��o das p�ginas na lista references
for x in range(0, len(references)):
    references[x] = int(references[x])

n = input("Digite o tamanho do frame de mem�ria: ")

#Cria��o do tamanho da lista de frames segundo o dado do usu�rio.
for i in range (0,n):
    frames.append(None)

#Caso o item na posi��o j da lista de references j� esteja na lista de frames,
#ocorre um Hit, caso contr�rio, o j � substitu� a p�gina mais antiga da lista
#de frames.
for j in references:
    print("Inserindo o "+str(j)+"\n")
    if (j in frames):
        print("Hit na p�gina "+str(j))
        contHit += 1
    else:
        print("Miss")
        frames[cont] = j
        cont += 1
        print frames
        contMiss += 1
    #Um pequeno verificador que garante que o cont nunca exceda o tamanho da
    #lista de frames-1.
    if (cont >= len(frames)):
        cont = 0
    print("")

    time.sleep(1)
    
print ("No total ocorream "+str(contHit)+" hit(s) e "+str(contMiss)+" miss(es).") 
