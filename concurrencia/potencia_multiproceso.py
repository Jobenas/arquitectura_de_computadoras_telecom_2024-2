from multiprocessing import Process
import time


def potencia(n: int) -> int:
    pot = 1

    for _ in range(n):
        pot = pot * n
    
    return pot


if __name__ == '__main__':
    p_num = 2
    valor = 100_000

    inicio = time.perf_counter()
    procesos = list()
    for i in range(p_num):
        proceso = Process(target=potencia, args=(valor // p_num, ))
        procesos.append(proceso)
    
    for proceso in procesos:
        proceso.start()

    for proceso in procesos:
        proceso.join()

    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion con multiproceso con {p_num} procesos: {t_ejecucion:0.3f} segundos")
