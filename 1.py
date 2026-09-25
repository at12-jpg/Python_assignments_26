#list of students name
student_names = ["Alien", "Atharva", "Aaryan", "Ayushi"]



#dictionary of students role number and details stored in tuple 
students = {
    1: ("Alien", "AI/DS", 85),
    2: ("Atharva", "CSE", 78), 
    3: ("Aaryan", "Cloud Computing", 83),
    4: ("Ayushi", "AI/DS", 70)
}

#addition of new student 
student_names.append("Aarav")
students[5] = ("Aarav", "CSE", 81)

#removing existing student
student_names.remove("Atharva")
del students[2]

#changes in existing students data
students[1] = ("Alien", "AI/DS", 99)

print(f"Student Names : {student_names}")

#display of list of students along with all of their details
print("Final Students Records:")

for roll_no, details in students.items():
    print("Roll Number:", roll_no)
    print("Name:", details[0])
    print("Branch:", details[1])
    print("Marks: ", details[2])
    print()