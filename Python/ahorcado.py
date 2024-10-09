
from typing import Union

palabras = ["arquitectura"]
intentos = 5
palabras_equivocadas = list()
palabras_correctas = list()

def ingresa_letra() -> str:
    while True:
        letra = input("Ingrese una letra: ")
        if len(letra) != 1:
            print("Ingrese solo una letra")
        elif letra.isnumeric():
            print("Debe ingresar letras y no numeros")
        else:
            break
    return letra

def imprime_estado(palabra: str, num_intentos: int, palabras_error: list[str]):
    print(f"{' '.join(l for l in palabra)}\nIntentos restantes: {num_intentos}\t\tLetras incorrectas: {', '.join(palabras_error)}")


def busca_letra(palabra: str, letra: str, lista_de_letras: list[str]) -> Union[list[str], bool]:
    palabra_encontrada = False
    for idx in range(len(palabra)):
        if letra == palabra[idx]:
            lista_de_letras[idx] = letra
            palabra_encontrada = True

    return lista_de_letras, palabra_encontrada


if __name__ == "__main__":
    print("Bienvenido al juego del ahorcado")
    palabra_objetivo = palabras[0]
    palabra_lista = ["_"] * len(palabra_objetivo)
    while True:
        imprime_estado(palabra_lista, intentos, palabras_equivocadas)
        letra_ingresada = ingresa_letra()

        if letra_ingresada in palabras_equivocadas and letra_ingresada in palabras_correctas:
            print("Letra ya ingresada")
            continue

        palabra_lista, encontrada = busca_letra(palabra_objetivo, letra_ingresada, palabra_lista)

        if not encontrada:
            intentos -= 1
            palabras_equivocadas.append(letra_ingresada)
            print("Letra ingresada no pertenece a la palabra")
        else:
            palabras_correctas.append(letra_ingresada)
        
        if intentos == 0:
            print("Lo siento, ha perdido el juego")
            exit(0)
        
        if "_" not in palabra_lista:
            print("Felicidades, ha ganado el juego!")
            exit(0)
