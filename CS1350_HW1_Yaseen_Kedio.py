grades = {"Alice": 87,"Bob": 65,"Carol": 92,"Dave": 78,"Eve": 55,"Frank": 88, "Grace": 71,"Henry": 95,"Ivy": 60,"Jack": 83}

print(grades.keys())

print(grades.values())
print("\n")
students_num= len(grades)

print(f"Total Students: {students_num}")

sum_grades = sum(grades.values())

print(f"Sum of Grades:{sum_grades}")

class_average= sum(grades.values()) /len(grades)

print(f"Class Average: {class_average:2f}") 

Highest_grades= max(grades.values()) 

print(f"Highest Grade: {Highest_grades}")

Lowest_grades = min(grades.values())

print(f"Lowest Grade: {Lowest_grades}")
print("\n")

#Part B
def get_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print("\n")

for student, grade in grades.items():
    print("\n")
    letter = get_letter(grade)
    print(f"{student} grade is a {letter} and their score is a {grade}")
    
passed = 0
failed = 0
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

for student , grade in grades.items():
    
    letter = get_letter(grade)
    
    if grade >= 60:
        passed +=1
    else: 
        failed +=1
        
    if letter == "A":
        count_a +=1
    elif letter == "B":
        count_b +=1
    elif letter == "C":
        count_c +=1
    elif letter == "D": 
        count_d +=1
    else:
        count_f +=1
        print("\n")
   
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"A grades: {count_a}")
print(f"B grades: {count_b}")
print(f"C grades: {count_c}")
print(f"D grades: {count_d}")
print(f"F grades: {count_f}")
   
top_student = ""  
top_grade = 0

for student, grade in grades.items():
    if grade > top_grade:
        top_grade = grade
        top_student = student
print("\n")

print(f"Top Student: {top_student} ({top_grade})")

bottom_student = ""
bottom_grade = 100
for student, grade in grades.items():
    if grade < bottom_grade:
        bottom_grade = grade
        
        bottom_student = student

print(f"Lowest scorer: {bottom_student} ({bottom_grade})")
print("\n")
print("\n")


print("\n")
for student, grade in grades.items():
    if grade >= class_average:
        print(f"the student {student} scored above average with a {grade} ")




