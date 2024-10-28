import socket

SOCK_BUFFER = 1024

def extrae_datos(data_cruda: bytes) -> list[int]:
    datos_str = data_cruda.decode("utf-8")
    datos_lista_str = datos_str.split(",")
    # datos_lista = [int(elemento) if elemento.isnumeric() else -1 for elemento in datos_lista_str]
    datos_lista = list()
    for elemento in datos_lista_str:
        if elemento.isnumeric():
            datos_lista.append(int(elemento))
        else:
            datos_lista.append(-1)

    return datos_lista


def valida_datos(data_procesada: list[int]) -> bool:
    if len(data_procesada) != 15:
        return False
    
    if -1 in data_procesada:
        return False
    
    return True


def calcula_nota(data_procesada: list[int]) -> float:
    notas_lab = data_procesada[1:13]
    e1 = data_procesada[13]
    e2 = data_procesada[14]

    nota_lab = sum(notas_lab) / len(notas_lab)
    nota_final = ((nota_lab * 5) + (e1 * 2.5) + (e2 * 2.5)) / 10

    return nota_final


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

        print(f"Conexion de {client_address[0]}:{client_address[1]}")

        try:
            while True:
                dato = conn.recv(SOCK_BUFFER)

                if dato:
                    notas = extrae_datos(dato)
                    if not valida_datos(notas):
                        conn.sendall("El dato ingresado no corresponde al formato requerido")
                    nota_final = calcula_nota(notas)
                    conn.sendall(f"{nota_final}".encode('utf-8'))
                else:
                    print("No hay más datos")
                    break
        except ConnectionResetError:
            print("El cliente ha cerrado la conexión de manera abrupta")
        finally:
            print("Cerrando la conexión")
            conn.close()