from multiprocessing import Process

class MeuProcesso(Process):

    #inicialização do processo
    def __init__(self):
        Process.__init__(self)


    # tudo o que o processo ira executar deve
    # estar no metodo run. Enquanto o run estiver
    # rodando, o processo esta em execução

    def run(self):
        print("Eu sou um processo!!! {}".format(self.name))

if __name__ == '__main__':

    processo = MeuProcesso()
    processo.start()
    processo.join()

    print("Pai finalizando...")