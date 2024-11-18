from multiprocessing import Process
import time

var = 0


def func(ident: int) -> None:
    global var
    var += 1
    print(f"Al ingresar al hilo {ident} - valor de var = {var}")
    time.sleep(1)
    # var -= 1
    # print(f"Al salir del hilo {ident} - valor de var = {var}")


if __name__ == '__main__':
    procesos = list()

    for i in range(5):
        proceso = Process(target=func, args=(i, ))
        procesos.append(proceso)

    for proceso in procesos:
        proceso.start()
    
    for proceso in procesos:
        proceso.join()

    print(f"Valor final de var: {var}")
