from multiprocessing import Process
import time


N = 200_000_000


def cuenta(n: int) -> None:
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    p1 = Process(target=cuenta, args=(N // 2, ))
    p2 = Process(target=cuenta, args=(N // 2, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f'Tiempo de ejecución: {t_ejecucion:0.5f} segundos')
