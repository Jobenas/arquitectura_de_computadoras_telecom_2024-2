import socket

SOCK_BUFFER = 1024


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
                    print(f"Recibi: {dato}")
                    conn.sendall(dato)
                else:
                    print("No hay más datos")
                    break
        except ConnectionResetError:
            print("El cliente ha cerrado la conexión de manera abrupta")
        finally:
            print("Cerrando la conexión")
            conn.close()