import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 5000)
    print(f"Conectandose a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    for i in range(20):
        msg = f"Mensaje {i + 1}"   
        sock.sendall(msg.encode('utf-8'))
        dato = sock.recv(SOCK_BUFFER)
        print(f"Recibi: {dato}")

        time.sleep(0.5)

    sock.close()
