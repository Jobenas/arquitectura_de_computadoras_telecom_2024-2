from threading import Thread
import time


CUENTA = 200_000_000


def cuenta(n: int):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.time()
    t1 = Thread(target=cuenta, args=(CUENTA // 2,))
    t2 = Thread(target=cuenta, args=(CUENTA // 2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fin = time.time()

    t_ejecucion = fin - inicio

    print(f'Tiempo de ejecución: {t_ejecucion:0.5f} segundos')
