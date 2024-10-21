import os


def escribe_csv(nombre: str):
    contenido = "v1,v2,v3\n1,2,3\n4,5,6\n7,8,9"
    with open(nombre, "w+") as f:
        f.write(contenido)


def lee_csv(nombre: str) -> str:
    with open(nombre, "r") as f:
        contenido = f.read()

    return contenido


if __name__ == '__main__':
    nombre = "prueba.csv"
    if not os.path.exists(nombre):
        escribe_csv(nombre)

    res = lee_csv(nombre)

    filas = res.split("\n")

    print(filas)

    total = 0
    cont = 0

    for fila in filas:
        elementos = fila.split(",")
        if not elementos[0].isnumeric():
            continue
        for elemento in elementos:
            numero = int(elemento)
            total += numero
            cont += 1
    
    print(f"Suma total es {total} y el promedio es {total / cont}")
