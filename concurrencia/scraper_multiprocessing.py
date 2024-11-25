from multiprocessing import cpu_count, Pool
import time

import requests


session = None


def set_global_session() -> None:
    global session
    if session is None:
        session = requests.Session()


def get_site(url: str) -> None:
    with session.get(url) as response:
        # print(f"Lei {len(response.content)} bytes de {url}")
        pass


def get_all_sites(sites: list[str]) -> None:
    with Pool(processes=cpu_count(), initializer=set_global_session) as pool:
        pool.map(get_site, sites)


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

    print(f"Descarga completa usando codigo multi proceso en {t_ejecucion:0.5f} segundos")
