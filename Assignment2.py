# Program Name: Assignment2.py
# Course: IT3883 W01
# Student Name: Daijah McDonald
# Assignment Number: Lab 2
# Due Date: 9/19/2025
# Purpose: Calculate averages for students and put them in order.
# Resources: N/A

# Open the file with the student scores in it
file = open('students.txt', 'r')
lines = file.readlines()
file.close()

# A list to hold each student's info
student_averages = []

# Go through each line in the file
for line in lines:
    parts = line.strip().split()  # Remove spaces and split by space
    name = parts[0]               
    scores = []                   
    for score in parts[1:]:     
        scores.append(int(score)) # Turn into integers for ease
    avg = sum(scores) / len(scores) # Get average
    student_averages.append([name, avg]) # Save name and average

# Sort students by average from highest to lowest
student_averages.sort(key=lambda x: x[1], reverse=True)

for student in student_averages:
    print(student[0], round(student[1], 2))
