import asyncio
import time


async def cuenta(idx: int):
    print(f"[{idx}] Uno")
    await asyncio.sleep(1)
    print(f"[{idx}] Dos")


async def main():
    # await asyncio.gather(cuenta(), cuenta(), cuenta())
    await asyncio.gather(*(cuenta(i) for i in range(3)))


if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    print(f"Tiempo total de ejecucion: {t_ejecucion:0.5f} segundos")
