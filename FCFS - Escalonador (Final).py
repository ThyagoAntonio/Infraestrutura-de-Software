# encoding: iso-8859-1

import time

cont = 0
filaProcessos = []

class processo:
    def __init__(self, nome, tempoExecucao, tempoChegada):
        self.nome = nome
        self.tempoExecucao = tempoExecucao
        self.tempoChegada = tempoChegada
        self.tempoInicio = 0
        self.tempoFinal = 0
        self.parar = False

    def executar(self):
        if(cont <= 9):
            return " 0"+str(cont)+"                 %s"%(self.nome)
        else:
            return " "+str(cont)+"                 %s"%(self.nome)

    def parar(self):
        self.parar=True

def FCFS(filaProcessos):
    tempoAtual = 0
    tempoOcioso = 0
    listaOcioso=[]
    listaPosicao=[]

    print("\nTempo         Processo em Execução")
    
    #Ordena a fila de processos baseado no tempo de chegada
    filaProcessos.sort(key=lambda x: x.tempoChegada)

    #corre a fila de processos já ordenada
    for p in range(0,len(filaProcessos)):

        #loop para executar o processo durante o tempo de execução
        while(filaProcessos[p].tempoExecucao>0):

            #verifica se algum processo já chegou no tempo atual
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
                    ocioso=processo("Tempo Ocioso",0,0)
                    ocioso.tempoInicio=ocioso.tempoChegada
                    ocioso.tempoFinal=tempoOcioso
                else:
                    ocioso=processo("Tempo Ocioso",0,filaProcessos[p-1].tempoFinal)
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
                # se tiver chegado ele executa o processo por 1s e subtrai do tempo de execucao
                time.sleep(1)
                filaProcessos[p].tempoExecucao-=1
                print filaProcessos[p].executar()
                tempoAtual+=1

                #se for o primeiro processo o tempo inicial é o tempo de chegada
                #+ o tempo ocioso anterior (caso n tenha somará 0)
                if(p==0):
                        filaProcessos[p].tempoInicio = filaProcessos[p].tempoChegada+tempoOcioso
                        tempoOcioso=0

                #se não for o primeiro processo o tempo incial é o tempo final
                #do processo anterior + o tempo ocioso do anterior
                else:

                    #so atualiza o tempo de inicio se o tempo que estiver for menor que
                    #o tempo final do anterior, se for maior é pq já foi atualizado.
                    if(filaProcessos[p].tempoInicio<filaProcessos[p-1].tempoFinal):
                        filaProcessos[p].tempoInicio = filaProcessos[p-1].tempoFinal+tempoOcioso
                        tempoOcioso=0

                # o tempo final sempre é igual ao tempo atual
                filaProcessos[p].tempoFinal = tempoAtual

            cont+=1

    #coloca os "processos ociosos" na lista para imprimir a tabela
    c=0
    for p in range(0,len(listaOcioso)):
        filaProcessos.insert(listaPosicao[p]+c,listaOcioso[p])
        c+=1
        
    # imprime a tabela
    print ""
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
        

    #faz os calculos de todos os tempos de espera
    somatorio=0
    c=0
    for p in range(0,len(filaProcessos)):
        tempoEspera = filaProcessos[p].tempoInicio-filaProcessos[p].tempoChegada
        print "Tempo de Espera do %s: %d"%(filaProcessos[p].nome,tempoEspera)
        somatorio+=tempoEspera
        c+=1
    
    print "\nTempo de Espera Médio: %.2f"%(float(somatorio)/float(c))
                                        
qtdProcessos = input("Digite a quantidade de processos desejados: ")
print("")
print("Digite o tempo de execução e o tempo de chegada (separados por espaço) do: \n")
for p in range(1, qtdProcessos+1):
    proc = raw_input("Processo "+str(p)+": ")
    proc = proc.split(" ")
    filaProcessos.append(processo(("Processo "+str(p)),int(proc[0]),int(proc[1])))

FCFS(filaProcessos)
