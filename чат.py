import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

clients = []
usernames = []

def handle_client(conn, addr):
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if message:
                broadcast(message, conn)
            else:
                remove_client(conn)
                break
        except:
            remove_client(conn)
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        index = clients.index(client_socket)
        username = usernames[index]
        usernames.remove(username)
        broadcast(f'{username} left the chat!'.encode('utf-8'), client_socket)

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f'Server is listening on {HOST}:{PORT}')

    while True:
        conn, addr = server.accept()
        print(f'Connected by {addr}')

        conn.send('NICK'.encode('utf-8'))
        username = conn.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(conn)

        broadcast(f'{username} joined the chat!'.encode('utf-8'), conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()