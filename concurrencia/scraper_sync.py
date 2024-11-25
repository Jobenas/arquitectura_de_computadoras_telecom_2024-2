import time

import requests


def get_site(url: str, session: requests.Session) -> None:
    with session.get(url) as response:
        # print(f"Lei {len(response.content)} bytes de {url}")
        pass


def get_all_sites(sites: list[str]) -> None:
    with requests.Session() as session:
        for site in sites:
            get_site(site, session)



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

    print(f"Descarga completa usando codigo sincrono en {t_ejecucion:0.5f} segundos")
