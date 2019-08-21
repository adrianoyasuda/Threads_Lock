from threading import Thread, Lock
import time
import random

acumulador = 0
repeticoes = 2000
lock1 = Lock()
lock2 = Lock()

# lock.release()


def incrementa():
    lock1.acquire()
    lock2.acquire()
    global acumulador
    acumulador += 1
    t = random.randint(1, 5)
    print("INC - Dormindo por {}s".format(t))
    # time.sleep(t)
    lock1.release()
    lock2.release()



def decrementa():
    lock2.acquire()
    lock1.acquire()
    global acumulador
    acumulador -= 1
    t = random.randint(1, 5)
    print("DEC - Dormindo por {}s".format(t))
    # time.sleep(t)
    lock2.release()
    lock1.release()


def incrementador():
    # lock.acquire()
    for i in range(repeticoes):
        incrementa()
    # lock.release()

def decrementador():
    # lock.acquire()
    for i in range(repeticoes):
        decrementa()
    # lock.release()


if __name__ == '__main__':
    t1 = Thread(target=incrementador)
    t2 = Thread(target=decrementador)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Resultado Final: {}".format(acumulador))
