import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("127.0.0.1", 65000))
serversocket.listen()

print("Server has been started")

try:
    while 1:
        clientsocket, address = serversocket.accept()
        print(f"Connection from {address} has been established.")
        clientsocket.send(bytes("You have connected to the server", "utf-8"))
except:
    print("Error")
finally:
    serversocket.close()

