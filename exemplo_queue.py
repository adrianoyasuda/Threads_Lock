from multiprocessing import Process, Queue
import time


class MeuProcesso(Process):
    def __init__(self, fila):
        Process.__init__(self)
        self.fila = fila

    def run(self):
        n=10
        while n>0:
            elem = self.fila.get()
            print("Filho -- Recebi: {}".format(elem))
            time.sleep(3)
            n-=1

if __name__ == '__main__':
    q = Queue()
    processo = MeuProcesso(q)
    processo.start()

    for a in range(10):
        lista=[]

        for z in range(10):
            lista.append(z)

        print("Pai--Enviando:{}".format(lista))
        q.put(lista)

    processo.join()
