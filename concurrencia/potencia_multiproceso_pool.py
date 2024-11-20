from multiprocessing import Pool, cpu_count
import time


def potencia(n: int) -> int:
    pot = 1

    for _ in range(n):
        pot = pot * n

    return pot


if __name__ == '__main__':
    workers = cpu_count() // 2
    tareas = 10_000
    valor = 100_000

    args = [valor // tareas] * tareas

    inicio = time.perf_counter()
    p = Pool(processes=workers)    
    res = p.map(potencia, args)
    p.close()
    p.join()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion con multiproceso usando {workers} procesos con {tareas} tareas: {t_ejecucion:0.3f} segundos")
