from threading import Thread, Semaphore
import random
import time

class Produtor(Thread):

    def __init__(self, recurso, semaforo):
        Thread.__init__(self)
        self.recurso = recurso
        self.semaforo = semaforo

    def run(self):
        for x in range(5):
            i = random.randint(1, 1000)
            print("Produzido {}".format(i))
            self.recurso.append(i)
            time.sleep(2)
            self.semaforo.release()


class Consumidor(Thread):

    def __init__(self, recurso, semaforo):
        Thread.__init__(self)
        self.recurso = recurso
        self.semaforo = semaforo

    def run(self):
        for x in range(5):
            self.semaforo.acquire()
            i = self.recurso.pop()
            print("Consumindo {}".format(i))
            time.sleep(3)


if __name__ == '__main__':

    recurso = []
    semaforo = Semaphore(0)

    produtor = Produtor(recurso, semaforo)
    consumidor = Consumidor(recurso, semaforo)

    produtor.start()
    consumidor.start()

    produtor.join()
    consumidor.join()
