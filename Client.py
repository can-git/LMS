import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    clientsocket.bind(("127.0.0.1", 65000))
    msg = clientsocket.recv(1024).decode("utf-8")
    print(msg)
except Exception as e:
    print(e)
finally:
    clientsocket.close()

