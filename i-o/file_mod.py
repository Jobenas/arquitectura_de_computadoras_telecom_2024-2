

def escribe_archivo(nombre_archivo: str, contenido: str):
    with open(nombre_archivo, "w+") as f:
        f.write(contenido)


def lee_archivo(nombre_archivo: str) -> str:
    f = open(nombre_archivo, "r")
    contenido = f.read()
    f.close()

    return contenido


if __name__ == '__main__':
    escribe_archivo("archivo_prueba.txt", "este es un archivo de prueba, con mas texto")

    contenido_archivo = lee_archivo("archivo_prueba.txt")

    print(f"El contenido del archivo es: {contenido_archivo}")
