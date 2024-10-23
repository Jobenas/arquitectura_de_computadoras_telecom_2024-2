from calcula_notas_finales import calcula_notas


if __name__ == '__main__':
    tiempos_iter = list()

    for _ in range(20):
        tiempos = calcula_notas()
        tiempos_iter.append(tiempos)

    tiempo_lectura_promedio = sum([tiempo[0] for tiempo in tiempos_iter]) / len(tiempos_iter)
    tiempo_procesamiento_promedio = sum([tiempo[1] for tiempo in tiempos_iter]) / len(tiempos_iter)
    tiempo_escritura_promedio = sum([tiempo[2] for tiempo in tiempos_iter]) / len(tiempos_iter)
    tiempo_total_promedio = sum([tiempo[3] for tiempo in tiempos_iter]) / len(tiempos_iter)

    porcentaje_tiempo_es_promedio = (tiempo_total_promedio - tiempo_procesamiento_promedio) / tiempo_total_promedio * 100

    print(f"Tiempo de lectura promedio: {tiempo_lectura_promedio} segundos")
    print(f"Tiempo de procesamiento promedio: {tiempo_procesamiento_promedio} segundos")
    print(f"Tiempo de escritura promedio: {tiempo_escritura_promedio} segundos")
    print(f"Tiempo total promedio: {tiempo_total_promedio} segundos")
    print(f"Porcentaje de tiempo de operaciones E/S promedio: {porcentaje_tiempo_es_promedio}%")
