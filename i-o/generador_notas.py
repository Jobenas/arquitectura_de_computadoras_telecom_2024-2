from random import randint
import time


if __name__ == '__main__':
    inicio = time.perf_counter()
    contenido = f"codigo,{','.join([f"lab_{i}" for i in range(1, 13)])},e1,e2\n"
    codigo_inicial = 20240001
    
    for i in range(500):
        codigo = codigo_inicial + i
        notas = [randint(0, 20) for _ in range(14)]
        fila = f"{codigo},{','.join([str(nota) for nota in notas])}\n"
        contenido += fila
    fin_procesamiento = time.perf_counter()
    
    with open("notas_parciales.csv", "w+") as f:
        f.write(contenido)
    
    fin = time.perf_counter()

    print(f"Tiempo de procesamiento: {fin_procesamiento - inicio} segundos")
    print(f"Tiempo de escritura de archivo: {fin - fin_procesamiento} segundos")
    print(f"Tiempo total: {fin - inicio} segundos")

    print(f"Porcentaje de tiempo de operaciones E/S: {(fin - fin_procesamiento) / (fin - inicio) * 100}%")
