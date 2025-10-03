# Program Name: Assignment3.py 
# Course: IT3883/Section W01
# Student Name: Daijah McDonald
# Assignment Number: Lab3
# Due Date: 10/02/ 2025
# Purpose: What does the program do (in a few sentences)? GUI that converts to km/L.
# List Specific resources used to complete the assignment. N/A

from tkinter import *

MPG_TO_KML = 0.425143707

def convert(event):
    """Convert mpg to km/L whenever user types"""
    val = entry.get()
    try:
        mpg = float(val)
        kml = mpg * MPG_TO_KML
        result_var.set(f"{kml:.4f} km/L")
    except:
        # if input is wrong, reset
        result_var.set("")

# main
top = Tk()
top.title("MPG to Km/L Converter")
top.geometry("250x120")

Label(top, text="Enter MPG:").pack(pady=5)
entry = Entry(top)
entry.pack(pady=5)

# label for result
result_var = StringVar()
Label(top, textvariable=result_var, fg="green").pack(pady=5)

# live update 
entry.bind("<KeyRelease>", convert)

top.mainloop()
