# Program Name: Assignment1.py 
# Course: IT3883/Section W01
# Student Name: Daijah McDonald
# Assignment Number: Lab1
# Due Date: 09/14/2025
# Purpose: This program implements a text-based menu for the user.
# List Specific resources used to complete the assignment.


    # empty buffer for input
buffer = ""
while True:
    print("\nMenu:")
    print("1. Append data to buffer")
    print("2. Clear buffer")
    print("3. Display buffer")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    # option 1: add data to buffer
    if choice == "1":
        data = input("Enter text to add: ")
        buffer += data
        print("Data added.")

    # option 2: clear the buffer
    elif choice == "2":
        buffer = ""
        print("Buffer cleared.")

    # option 3: show the buffer as is
    elif choice == "3":
        print("Current buffer:", buffer)

    # option 4: exit the program
    elif choice == "4":
        print("Exiting program.")
        break



