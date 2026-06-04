# a teacher is taking attendance of students. strength of class is 30 , every time he needs to insert whether students is present or absent . count the total number of students present in the class and display it at the end of the class as wlll as absent  students.        
student = int(input("Enter the number of students in the class: "))
attendance = 0
present_students = 0
absent_students = 0

while attendance < student:
    attendence += 1
    status = input("Is the student present? (yes/no): ").strip().lower()

    if status == 'p' or status == 'present':
        present_students += 1
    elif status == 'a' or status == 'absent':
        absent_students += 1
    else:
        print("Invalid input. Please 'p' for present and 'a' for absent.")
        attendance -= 1  # Decrement attendance to retry for the same student
        
print("\n Attendance Summary:")
print(f"Present Students: {present_students}")
print(f"Absent Students: {absent_students}")
