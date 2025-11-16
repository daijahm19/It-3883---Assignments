# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Daijah McDonald
# Assignment Number: Lab 5
# Due Date: 11/16/2025
# Purpose: What does the program do (in a few sentences)? Program makes a database of temperatures and takes the average of 2 days.
# List Specific resources used to complete the assignment.



import sqlite3

db = sqlite3.connect("temps.db")
task = db.cursor()

task.execute("DROP TABLE IF EXISTS temps")

task.execute("""
    CREATE TABLE temps(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT,
        temp REAL
    )
""")

file = open("Assignment5input.txt", "r")
lines = file.readlines()

for line in lines:
    pieces = line.strip().split()
    d = pieces[0]
    t = float(pieces[1])
    task.execute("INSERT INTO temps(day, temp) VALUES(?, ?)", (d, t))

db.commit()

task.execute("SELECT AVG(temp) FROM temps WHERE day='Sunday'")
sunday_average = task.fetchone()[0]

task.execute("SELECT AVG(temp) FROM temps WHERE day='Thursday'")
thursday_average = task.fetchone()[0]

print("Average Sunday Temp:", round(sunday_average, 2))
print("Average Thursday Temp:", round(thursday_average, 2))

db.close()
