# encoding: iso-8859-1

import time

cont = 0
contHit = 0
contMiss = 0
references = []
hit = []
miss = []
frames = []

ref = raw_input("Digite a string de referências separadas por espaço: ")
references = ref.split(" ")

#Inserção das páginas na lista references
for x in range(0, len(references)):
    references[x] = int(references[x])

n = input("Digite o tamanho do frame de memória: ")

for j in range (0,len(references)):
    print("Inserindo o "+str(references[j])+"\n")
    if (references[j] in frames):
        print("Hit na página "+str(references[j]))
        contHit += 1
        hit.append(j)
        
    else:
        print("Miss")
        contMiss += 1
        #se a lista de frames estiver com espaço vazio entra no if
        if(len(frames)!=n):
            frames.append(references[j])
            miss.append(references[j])
		
        #n eh tamanho do frame de memoria
        #j eh o ponteiro que está realizando a leitura do vetor references
        #pont eh o ponteiro que ira percorrer references da presente posição ate o inicio

        
        #lista frames não possui espaços vazios
        else:        
            pont = j-1
            framestemp=[]
            while(len(framestemp)<n):
                if((references[pont] in framestemp) == False): ##testa se o valor anterior ao j não está na lista framestemp
                    framestemp.append(references[pont])
                pont-=1
			
            num = frames.index(framestemp[-1]) #armazena em num o valor do indice na lista do valor a ser retirado, que se encontra na ultima posicao da lista temporaria
            del frames[num] #apaga o valor que é pra sair da lista para não aumentar o tamanho da lista
            frames.insert(num,references[j]) #insere o novo valor na lista na posição em que estava o antigo 
            del framestemp #deleta a lista temporaria
            
			
        print frames
        
    print("")

    time.sleep(1)
    
    
print ("No total ocorream "+str(contHit)+" hit(s) e "+str(contMiss)+" miss(es).") 
