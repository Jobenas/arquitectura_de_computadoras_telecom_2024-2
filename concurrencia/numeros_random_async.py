import asyncio
from random import randint, seed

c = (
    "\033[0m", # Fin del color
    "\033[36m", # Cyan
    "\033[91m", # Rojo
    "\033[35m", # Magenta
)


async def makerandom(idx: int, threshold: int = 0) -> int:
    print(c[idx + 1] + f"Iniciando makerandom({idx})")
    i = randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i}, muy bajo, reintando")
        await asyncio.sleep(randint(1, 4))
        i = randint(0, 10)
    print(c[idx + 1] + f"-----> Terminando: makerandom({idx}) == {i}" + c[0])

    return i


async def main():
    # res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    res = await asyncio.gather(*(makerandom(i, randint(7, 9)) for i in range(3)))

    return res


if __name__ == '__main__':
    # seed(1337)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
