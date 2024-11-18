from threading import Thread
import time

var = 0


def func(ident: int) -> None:
    global var
    var += 1
    print(f"Al ingresar al hilo {ident} - valor de var = {var}")
    time.sleep(1)
    var -= 1
    print(f"Al salir del hilo {ident} - valor de var = {var}")


if __name__ == '__main__':
    hilos = list()

    for i in range(5):
        hilo = Thread(target=func, args=(i, ))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()
    
    for hilo in hilos:
        hilo.join()
