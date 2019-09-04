from multiprocessing import Process
from threading import  Thread


class MeuProcesso(Process):

    def __init__(self, lista):
        Process.__init__(self)
        self.lista = lista

    def run(self):
        print("Processo... {}".format(self.lista))
        for a in range(5, 10, 1):
            self.lista.append(a)

        print("Fim - Processo...{}".format(self.lista))

if __name__ == '__main__':
    lista = [1,2,3,4]
    processo = MeuProcesso(lista)
    processo.start()
    processo.join()
    print("Pai...{}".format(lista))

