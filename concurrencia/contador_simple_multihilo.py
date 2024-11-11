from threading import Thread
import time


def cuenta(idx: int):
    print(f"[{idx}] Uno")
    time.sleep(1)
    print(f"[{idx}] Dos")


def main():
    threads = list()
    for i in range(3):
        thread = Thread(target=cuenta, args=(i,))
        threads.append(thread)

    for thread in threads:
        thread.start()
        thread.join()

    # for thread in threads:
    #     thread.join()


if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion: {t_ejecucion:0.5f} segundos")
