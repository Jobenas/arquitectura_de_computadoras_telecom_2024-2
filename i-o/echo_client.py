import socket

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 5000)
    print(f"Conectandose a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    # msg = "Hola mundo"
    msg = "20240001,13,15,6,8,7,0,18,20,0,14,15,8,3,13"

    sock.sendall(msg.encode('utf-8'))
    dato = sock.recv(SOCK_BUFFER)

    sock.close()

    print(f"Recibi: {dato}")
