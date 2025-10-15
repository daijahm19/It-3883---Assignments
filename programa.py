# Program Name: Assignment4.py 
# Course: IT3883/Section WO1
# Student Name: Daijah McDonald
# Assignment Number: Lab 4
# Due Date: 10/26/ 2025
# Purpose: What does the program do (in a few sentences)? One program takes in a message and the other returns that message in all caps. 
# List Specific resources used to complete the assignment. N/A 



import socket

port_number = 45001
ip_address = "127.0.0.1"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, port_number))

user_input = input("Type a message to send to Program B: ")
client_socket.sendall(user_input.encode())

reply = client_socket.recv(1024)
print("From Program B:", reply.decode())

client_socket.close()