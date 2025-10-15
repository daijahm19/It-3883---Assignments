import socket

port_number = 45001
ip_address = "127.0.0.1"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port_number))
server_socket.listen()

print("Program B is accepting messages...")

conn, addr = server_socket.accept()
print("Connection from:", addr)

received = conn.recv(1024)
message = received.decode()
print("Received:", message)

upper_message = message.upper()
conn.sendall(upper_message.encode())

conn.close()
server_socket.close()