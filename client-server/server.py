import socket
import threading
import des_algorithm

"""
Title
-----
    Client-Server server side.

Author
-------
    Rafał Kreft

Description
-----------
    The part of the project responsible for client-server communication
    from the server side, handling many client connections, decryption,
    receiving client's messages and printing it in console.

Sources
---------------------------
https://docs.python.org/3/library/socket.html
https://docs.python.org/3/library/threading.html
https://www.youtube.com/watch?v=3QiPPX-KeSc
"""

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'Disconnected!'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

des = des_algorithm.DesAlgorithm('some key')


def handle_client(conn, addr):
    """
    Function for client-server connection handling.
    Decrypts and displays messages received from the client.

    Parameters
    ----------

        conn : socket object
            Socket object needed to handle client-server connection

        addr : connection address object
            Object containing host and port address

    Returns
    -------
        The function returns nothing
    """

    print(f"New connection {addr}")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            msg = des.decrypt(msg)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{ADDR}] {msg}")

    conn.close()


def start():
    """
    The function that starts the server listening.
    Runs on multiple threads, allowing to serve multiple clients.

    Parameters
    ----------
        The function has no parameters

    Returns
    -------
        The function returns nothing
    """
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


print("STARTING SERVER...")
start()
