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
Encapsulation protects requisition data, SRP keeps methods focused, and abstraction hides complexity.
The design makes the system easy to understand, update, and extend.
