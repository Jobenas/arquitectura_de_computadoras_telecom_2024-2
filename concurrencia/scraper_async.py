import asyncio
import time

import aiohttp


async def get_site(url: str, session: aiohttp.ClientSession) -> None:
    async with session.get(url) as response:
        content = await response.text()
        # print(f"Lei {len(content)} bytes de {url}")
        pass

    
async def get_all_sites(sites: str) -> None:
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[get_site(site, session) for site in sites])


if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://www.python.org/",
    ] * 80

    inicio = time.perf_counter()
    asyncio.run(get_all_sites(sites))
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Descarga completa usando codigo asincrono en {t_ejecucion:0.5f} segundos")

