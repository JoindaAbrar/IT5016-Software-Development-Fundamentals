Requisition Management System

1. Overview
This project creates a basic requisition‑management system using OOP.
Each requisition stores staff details, items, total cost, status, and approval reference.
The system allows submitting requisitions, updating them, responding to them, and viewing statistics.

2. Software Design Principles
Encapsulation
All requisition data (date, staff ID, items, total, status) is stored inside the object.
Updates happen only through methods like staff_info(), update_status(), and respond_requisition().

Single Responsibility Principle
Each method performs one clear task:

staff_info() → update staff details

requisitions_details() → update items and total

requisition_approval() → apply approval rules

respond_requisition() → manager decision

display_requisitions() → show all requisitions

requisition_statistics() → show summary counts

Abstraction
The class hides internal logic such as:

ID generation

Total cost calculation

Approval reference creation

Users interact only through simple methods.

Object Interaction
Multiple requisition objects are stored in a list and processed together for:

Display

Statistics

Manager approval

3. Summary
This system demonstrates how OOP helps organize data and behavior into a clear structure.

=====================================================================================

README – Student Attendance Management System
1. Overview
This project implements a basic student‑attendance management system using Object‑Oriented Programming (OOP).
It allows creating student records, updating their attendance and course, displaying all students, and calculating average attendance.

2. Software Design Principles
Encapsulation
Each student’s data (ID, name, course, attendance) is stored inside the Student object.
Updates happen only through methods like:

update_attendance()

update_course()

This protects the internal state of each student record.

Single Responsibility Principle
Each part of the program has one clear job:

Student class → stores and updates student information

display_students() → prints all student records

calculate_average_attendance() → computes average attendance

Updatestudent_by_id() → updates a specific student

This keeps the code simple and easy to maintain.

Abstraction
The user interacts with simple functions and methods.
They do not need to know how IDs are generated or how attendance is stored internally.

Object Interaction
Multiple Student objects are stored in a list.
Functions operate on this list to:

Display all students

Update a specific student

Calculate average attendance

This shows how objects work together in an OOP system.

3. Summary
This student‑attendance system demonstrates key OOP principles:

Encapsulation protects student data

SRP keeps functions focused

Abstraction hides complexity

Object interaction supports multi‑student operations

The design is simple, clear, and easy to extend.
Encapsulation protects requisition data, SRP keeps methods focused, and abstraction hides complexity.
The design makes the system easy to understand, update, and extend.
