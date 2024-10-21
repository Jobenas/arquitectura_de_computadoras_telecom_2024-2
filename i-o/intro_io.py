import time


if __name__ == '__main__':
    inicio = time.perf_counter()
    a = 3
    b = 4
    c = a + b
    inicio_print = time.perf_counter()
    print(f"El resultado de la operacion es {c}")
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos\tTiempo de print: {fin - inicio_print} segundos\tPorcentaje de uso de E/S: {((fin - inicio_print)/(fin - inicio)) * 100}%")
