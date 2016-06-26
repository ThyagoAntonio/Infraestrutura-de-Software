# encoding: iso-8859-1

import time

cont = 0
filaProcessos = []

class processo:
    def __init__(self,nome,tempoExecucao,tempoChegada,quantum):
        self.nome=nome
        self.tempoExecucao=tempoExecucao
        self.tempoChegada=tempoChegada
        self.tempoInicio=0
        self.tempoFinal=0
        self.tempoEspera=0
        self.quantum=quantum

    def executar(self):
        if(cont <= 9):
            return " 0"+str(cont)+"                 %s"%(self.nome)
        else:
            return " "+str(cont)+"                 %s"%(self.nome)

def RR(filaProcessos):
    quantidadeProcessos = 3
    tempoAtual = 0
    tempoOcioso=0
    listaOcioso=[]
    listaPosicao=[]
    p=0

    print("\nTempo         Processo em Execução")

    #ordena a lista baseado no tempo de chegada
    filaProcessos.sort(key=lambda x: x.tempoChegada)

    #corre a fila de processos ordenada
    while(p<len(filaProcessos)):
        
        if(filaProcessos[p].quantum > filaProcessos[p].tempoExecucao):
            filaProcessos[p].quantum = filaProcessos[p].tempoExecucao

        while(filaProcessos[p].quantum>0):
            if(filaProcessos[p].tempoChegada > tempoAtual):
                # se não tiver chegado ele executa tempo ocioso
                time.sleep(1)
                global cont
                if (cont <= 9):
                    print " 0"+str(cont)+"              Nenhum (Ocioso)"
                else:
                    print " 0"+str(cont)+"              Nenhum (Ocioso)"
                tempoOcioso+=1
                tempoAtual+=1

                #cria um 'processo ocioso" para imprimir na tabela final
                #se for o primeiro processo o tempo de chegada é 0
                #se não o tempo inicial é o final do último processo
                if(p==0):
                    ocioso=processo("Tempo Ocioso",0,0,0)
                else:
                    ocioso=processo("Tempo Ocioso",0,filaProcessos[p-1].tempoFinal,0)

                ocioso.tempoInicio=ocioso.tempoChegada
                ocioso.tempoFinal=tempoAtual

                #se a duração do tempo ocioso é maior que é 1
                #tira o último objeto 'tempo ocioso' da lista e o substitui
                #pelo com o tempo de duração certa. 
                if(tempoOcioso>1):
                    listaOcioso.pop()
                    listaPosicao.pop()

                #adiciona o objeto de 'tempo ocioso' na lista e a sua posição    
                listaOcioso.append(ocioso)
                listaPosicao.append(p)
                    
            else:
                #executa o proceso
                time.sleep(1)
                filaProcessos[p].tempoExecucao-=1
                filaProcessos[p].quantum-=1
                print filaProcessos[p].executar()
                if(filaProcessos[p].quantum == 0):
                    print("")
                tempoAtual+=1
                #atualiza tempo inicio
                if(p==0):
                    filaProcessos[p].tempoInicio = filaProcessos[p].tempoChegada+tempoOcioso
                    tempoOcioso=0
                else:
                    if(filaProcessos[p].tempoInicio<filaProcessos[p-1].tempoFinal):
                        filaProcessos[p].tempoInicio = filaProcessos[p-1].tempoFinal+tempoOcioso
                        tempoOcioso=0

                # atualiza o tempo final e calcula o tempo de espera desse processo
                filaProcessos[p].tempoFinal = tempoAtual
                filaProcessos[p].tempoEspera = filaProcessos[p].tempoInicio - filaProcessos[p].tempoChegada

                #Se tiver acabado o quanto e o tempo de execucao n
                #coloca o processo no final da fila.
                if(filaProcessos[p].quantum==0 and filaProcessos[p].tempoExecucao > 0):
                    novoProcesso = processo(filaProcessos[p].nome,filaProcessos[p].tempoExecucao,
                             filaProcessos[p].tempoFinal,quantum)
                    novoProcesso.quantum = quantum
                    filaProcessos.append(novoProcesso)
                    #ordena a lista baseado no tempo de chegada
                    filaProcessos.sort(key=lambda x: x.tempoChegada)
            cont+=1
        p+=1
                
    #coloca os "processos ociosos" na lista para imprimir a tabela
    c=0
    for p in range(0,len(listaOcioso)):
        filaProcessos.insert(listaPosicao[p]+c,listaOcioso[p])
        c+=1
    
    #imprime a tabela
    print""
    print("Intervalo de Tempo entre os Processos\n")
    for p in range(0,len(filaProcessos)):
        if(filaProcessos[p].tempoInicio <= 9 and filaProcessos[p].tempoFinal <= 9):
            print "0%d - %s - 0%d"%(filaProcessos[p].tempoInicio, filaProcessos[p].nome,filaProcessos[p].tempoFinal)
        elif(filaProcessos[p].tempoInicio <= 9):
            print "0%d - %s - %d"%(filaProcessos[p].tempoInicio, filaProcessos[p].nome,filaProcessos[p].tempoFinal)
        elif(filaProcessos[p].tempoFinal <= 9):
            print "%d - %s - 0%d"%(filaProcessos[p].tempoInicio, filaProcessos[p].nome,filaProcessos[p].tempoFinal)
        else:
            print "%d - %s - %d"%(filaProcessos[p].tempoInicio, filaProcessos[p].nome,filaProcessos[p].tempoFinal)

    print("")

    #tira os processos ociosos da lista para fazer o calculo do tempo de espera
    for p in range(0,len(listaOcioso)):
        filaProcessos.pop(listaPosicao[p])

    
    #calcula tempo de espera
    tempoEspera=0
    resultado=[]
    somatorio=0
    for i in range(0,quantidadeProcessos):
        for p in range(0,len(filaProcessos)):
            if(filaProcessos[p].nome == "Processo %s"%(i+1)):
                tempoEspera+=filaProcessos[p].tempoEspera
        resultado.append(tempoEspera)
        print "Tempo de Espera do Processo %s: %d"%(i+1,tempoEspera)
        somatorio+=tempoEspera
        tempoEspera=0

    print "\nTempo de Espera Médio: %.2f"%(float(somatorio)/quantidadeProcessos)

qtdProcessos = input("Digite a quantidade de processos desejados: ")
quantum = input("Digite o quantum desejado: ")
print("")
print("Digite o tempo de execução e o tempo de chegada (separados por espaço) do: \n")
for p in range(1, qtdProcessos+1):
    proc = raw_input("Processo "+str(p)+": ")
    proc = proc.split(" ")
    filaProcessos.append(processo(("Processo "+str(p)),int(proc[0]),int(proc[1]),quantum))

RR(filaProcessos)

                
                
