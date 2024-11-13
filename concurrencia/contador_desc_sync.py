import time


CUENTA = 70_000_000


def cuenta(n: int):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.time()
    cuenta(CUENTA)
    fin = time.time()

    t_ejecucion = fin - inicio

    print(f'Tiempo de ejecución: {t_ejecucion:0.5f} segundos')
