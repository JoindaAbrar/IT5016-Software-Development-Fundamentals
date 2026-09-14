"""
Project Name: Student Attendance Tracking System Prototype
Description: This program creates a prototype for tracking student attendance
             for a training institute.
Author: Sana Alyaseri
Date: 2 April 2026
"""
import random
counter = 200
studentList = []
class Student:
    def __init__(self, student_name, attendance, course):
        self.student_id = random.randint(100, 999)
        self.student_name = student_name
        self.attendance = attendance
        self.course = course
# This function reads student information and stores attendance
    def add_student_attendance(self):

        st_name= " "

        while True:
            st_name= input("Enter student name (or type done to stop): ")
            if st_name== "done":
                break
            self.student_name = st_name
            self.attendance = int(input("Enter attendance percentage: "))
            self.course = input("Enter course name: ")
            studentList.append((self.student_id, self.student_name, self.attendance, self.course))

        


    def calculate_average_attendance(self):
        

        total = 0
        count = 0

        for student in studentList:
            total += student[2]
            count += 1

        if count == 0:
            return 0

        average = total / count
        return average


    def update_attendance(self):
        
        message = ""

        update_id = int(input("Enter student ID to update attendance: "))

        for i in range(len(studentList)):
            if studentList[i][0] == update_id:
                new_attendance = int(input("Enter new attendance percentage: "))
                new_course = input("Enter new course name: ")

                studentList[i] = (studentList[i][0], studentList[i][1], new_attendance, new_course)
                message = "Updated successfully"
                break
            else:
                message = "Student not found"

        print(message)
        


    def display_student_list(self):
        

        print("\n--- Student Attendance Records ---")
        for student in studentList:
            print(f"Student ID: {student[0]}")
            print(f"Student Name: {student[1]}")
            print(f"Attendance: {student[2]}%")
            print(f"Course: {student[3]}")
            print("--------------------------")

        avg = self.calculate_average_attendance()
        print(f"\nThe average attendance is: {avg}%")

# Create an instance of the Student class and display the student list
student1 = Student("", 0, "")
student1.add_student_attendance()

student1.display_student_list()