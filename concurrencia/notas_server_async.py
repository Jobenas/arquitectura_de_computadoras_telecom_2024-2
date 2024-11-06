import asyncio
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


async def handle_client(reader, writer):
    print("Cliente conectado")

    while True:
        msg_bytes = await reader.read(SOCK_BUFFER)
        if msg_bytes:
            notas = extrae_datos(msg_bytes)
            if not valida_datos(notas):
                writer.write("El dato ingresado no corresponde al formato requerido".encode("utf-8"))
                await writer.drain()
                continue
            nota_final = calcula_nota(notas)
            writer.write(f"{nota_final}".encode("utf-8"))
            await writer.drain()
        else:
            print("No hay mas datos del cliente")
            break

    writer.close()
    await writer.wait_closed()

    print("conexion cerrada")


async def main():
    server_address = ("0.0.0.0", 5000)

    server = await asyncio.start_server(handle_client, server_address[0], server_address[1])

    async with server:
        print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
