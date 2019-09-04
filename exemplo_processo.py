import multiprocessing
import time
import os

def funcao(i):

    #Pegando id do processo atual(filho)
    id = os.getpid()
    #pegando id do processo pai
    ppid = os.getppid()
    nome = multiprocessing.current_process().name
    print("{} - Eu sou o processo {} id={} ppid={}".format(nome, i, id, ppid))
    time.sleep(120)

if __name__ == '__main__':
    processos = []

    # pegando o id do processo atual
    id = os.getpid()
    print("Eu sou o processo pai id={}".format(id))
    for i in range(5):
        processo = multiprocessing.Process(name="Processinho {}".format(i),
                                           target=funcao, args=(i,))

        processo.start()

        print(processo.pid)
        processos.append(processo)


    time.sleep(10)

    for processo in processos:
        if(processo.is_alive()):
            print("Terminando processo {}".format(processo.pid))
            processo.join()

    for processo in processos:
        processo.join()

    print("Pai finalizando...!!!")