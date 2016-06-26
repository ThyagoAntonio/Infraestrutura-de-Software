# encoding: iso-8859-1

import time

cont = 0
contHit = 0
contMiss = 0
frames = []

ref = raw_input("Digite a string de referências separadas por espaço: ")
references = ref.split(" ")

#Inserção das páginas na lista references
for x in range(0, len(references)):
    references[x] = int(references[x])

n = input("Digite o tamanho do frame de memória: ")

#Criação do tamanho da lista de frames segundo o dado do usuário.
for i in range (0,n):
    frames.append(None)

#Caso o item na posição j da lista de references já esteja na lista de frames,
#ocorre um Hit, caso contrário, o j é substituí a página mais antiga da lista
#de frames.
for j in references:
    print("Inserindo o "+str(j)+"\n")
    if (j in frames):
        print("Hit na página "+str(j))
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
