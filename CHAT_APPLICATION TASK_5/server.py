import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen()

clients = []
names = []

print("Chat server started...")
print("Waiting for clients...")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            name = names[index]
            names.remove(name)

            broadcast(f"{name} left the chat.".encode(), client)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NAME".encode())
        name = client.recv(1024).decode()

        names.append(name)
        clients.append(client)

        print(f"Name: {name}")

        client.send("Connected to the chat!".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()
