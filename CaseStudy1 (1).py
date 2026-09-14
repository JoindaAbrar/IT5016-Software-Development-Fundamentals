"""
A training institute wants to create a simple prototype system to record and manage student attendance. The institute needs to keep track of student information such as student ID, student name, course name, and attendance percentage.
The system should allow staff to:
1.	Add student attendance records by entering the student’s name, attendance percentage, and course name. 
2.	Automatically generate a unique student ID for each student record. 
3.	Store all student records in a list for later use. 
4.	Update an existing student record by searching using the student ID and modifying the attendance percentage or course details. 
5.	Display all stored student records clearly for review. 
6.	Calculate the average attendance percentage for all recorded students. 

"""
# author: Sana Alyaseri
import random
Students = []  # List to store student records
# the class to represent a student record
class Student:
    def __init__(self, name, course_name, attendance_percentage):
        self.student_id = random.randint(1000, 9999)  # Generate a unique student ID
        self.name = name
        self.course_name = course_name
        self.attendance_percentage = attendance_percentage

    def update_attendance(self, new_attendance_percentage):
        self.attendance_percentage = new_attendance_percentage

    def update_course(self, new_course_name):
        self.course_name = new_course_name

# function to display all student records
def display_students(Students_list):
    print("Student Records:")
    for student in Students:
        print("Student ID : ", student.student_id)
        print("Student Name : ", student.name)
        print("Course Name : ", student.course_name)
        print("Attendance : ", student.attendance_percentage, "%")

# function to calculate the average attendance percentage
def calculate_average_attendance(Slist):
    if len(Slist) == 0:
        return 0
    total = sum(i.attendance_percentage for i in Slist)
    avg = total / len(Slist)
    return avg

def Updatestudent_by_id(Slist, key):
    flag=False
    for student in Slist:
        if student.student_id == key:
            student.update_attendance(int(input("Enter new attendance percentage: ")))
            student.update_course(input("Enter new course name: "))
            flag=True
            break
    if not flag:
        print("Student not found")

        


# the main program
st1=Student("John Doe", "Mathematics", 85)
#add the student to the list
Students.append(st1)
st2=Student("Jane Smith", "Physics", 90)
Students.append(st2)
st3=Student("Alice Johnson", "Chemistry", 75)
Students.append(st3)
display_students(Students)
print("Average Attendance:", calculate_average_attendance(Students), "%")
st3.update_attendance(80)
st3.update_course("Biology")
print("\nAfter updating Alice's attendance and course:")
display_students(Students)
print("Average Attendance:", calculate_average_attendance(Students), "%")
key = int(input("Student ID to search for: "))
Updatestudent_by_id(Students, key)
display_students(Students)