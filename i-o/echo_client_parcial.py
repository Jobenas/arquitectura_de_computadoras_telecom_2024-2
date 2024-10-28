import socket

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 5000)
    print(f"Conectandose a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "Hola mundo"
    msg_bytes = msg.encode("utf-8")
    cantidad_esperada = len(msg_bytes)
    cantidad_recibida = 0
    dato_total_bytes = b''

    sock.sendall(msg_bytes)

    while cantidad_recibida < cantidad_esperada:
        dato = sock.recv(SOCK_BUFFER)
        print(f"Recibi parcialmente: {dato}")
        cantidad_recibida += len(dato)
        dato_total_bytes += dato

    sock.close()

    print(f"Recibi: {dato_total_bytes.decode('utf-8')}")
