from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
import threading
import time

import requests

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def get_site(url: str):
    session = get_session()
    with session.get(url) as response:
        #  print(f"Lei {len(response.content)} bytes de {url}")
        pass


def get_all_sites(sites: list[str]):
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        executor.map(get_site, sites)


if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://www.python.org/",
    ] * 80

    inicio = time.perf_counter()
    get_all_sites(sites)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Descarga completa usando codigo multi hilo en {t_ejecucion:0.5f} segundos")

