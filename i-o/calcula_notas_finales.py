import time


def calcula_notas() -> list:
    inicio = time.perf_counter()
    with open("notas_parciales.csv", "r") as f:
        contenido = f.read()
    fin_lectura = time.perf_counter()

    filas = contenido.split("\n")

    notas_finales = []

    for fila in filas:
        if len(fila) == 0:
            continue
        elementos = fila.split(",")
        if elementos[0] == "codigo":
            continue
        codigo = elementos[0]
        notas = [int(nota) for nota in elementos[1:]]
        nota_lab = sum(notas[:12]) / len(notas[:12])
        e1 = notas[12]
        e2 = notas[13]

        nota_final = ((nota_lab * 5) + (e1 * 2.5) + (e2 * 2.5)) / 10
        fila = f"{codigo},{nota_final}\n"
        notas_finales.append(fila)

    contenido = f"codigo,nota_final\n{"".join(notas_finales)}" 
    fin_procesamiento = time.perf_counter()

    with open("notas_finales.csv", "w+") as f:
        f.write(contenido)

    fin = time.perf_counter()

    tiempo_lectura = fin_lectura - inicio
    tiempo_procesamiento = fin_procesamiento - fin_lectura
    tiempo_escritura = fin - fin_procesamiento
    tiempo_total = fin - inicio

    return [tiempo_lectura, tiempo_procesamiento, tiempo_escritura, tiempo_total]


if __name__ == '__main__':
    tiempos = calcula_notas()

    print(f"Tiempo de lectura de archivo: {tiempos[0]} segundos")
    print(f"Tiempo de procesamiento: {tiempos[1]} segundos")
    print(f"Tiempo de escritura de archivo: {tiempos[2]} segundos")
    print(f"Tiempo total: {tiempos[3]} segundos")

    print(f"Porcentaje de tiempo de operaciones E/S: {(tiempos[3] - tiempos[1]) / (tiempos[3]) * 100}%")
