import time


def potencia(n: int) -> int:
    pot = 1

    for i in range(n):
        pot = pot * n
    
    return pot


if __name__ == '__main__':
    inicio = time.perf_counter()
    potencia(100_000)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion: {t_ejecucion:0.3f} segundos")