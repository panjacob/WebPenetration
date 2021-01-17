import socket
import des_algorithm

"""
Title
-----
    Client-Server client side.

Author
-------
    Rafał Kreft
    
Description
-----------
    The part of the project responsible for client-server communication
    from the client side, receiving user input data, encryption
    and sending it to server.
       
Sources
---------------------------
https://docs.python.org/3/library/socket.html
https://www.youtube.com/watch?v=3QiPPX-KeSc
"""

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'Disconnected!'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

des = des_algorithm.DesAlgorithm('some key')


def send(msg):
    """
    Function for sending encrypted messages to server.

    Parameters
    ----------

        msg : String
            String containing client message.

    Returns
    -------
        The function returns nothing
    """
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


"""
    Loop for receiving client input and sending it to server.
"""
while True:
    msg = input(":")
    send(des.encrypt(msg))
