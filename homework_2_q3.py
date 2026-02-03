# Students and their registered courses
from re import U


registrations = {
"Alice": {"CS101", "CS201", "MATH101"},
"Bob": {"CS101", "MATH101", "PHYS101"},
"Carol": {"CS201", "CS301", "MATH201"},
"Dave": {"CS101", "CS201", "MATH101", "PHYS101"},
"Eve": {"CS301", "MATH201", "MATH301"}
}

# Course prerequisites (must have taken these BEFORE registering)
prerequisites = {
"CS101": set(), # No prerequisites
"CS201": {"CS101"}, # Must have CS101
"CS301": {"CS201"}, # Must have CS201
"MATH101": set(), # No prerequisites
"MATH201": {"MATH101"}, # Must have MATH101
"MATH301": {"MATH201"}, # Must have MATH201
"PHYS101": {"MATH101"} # Must have MATH101
}
# Course capacities and current enrollment
capacity = {"CS101": 30, "CS201": 25, "CS301": 20, "MATH101": 35, "MATH201": 25,
"MATH301": 20, "PHYS101": 30}

# Find all unique courses that have at least one student enrolled (use set union across all students)

print("=== Part A: Set Operations ===")

# 1. All courses with enrollment
all_courses = set()
for courses in registrations.values():
    all_courses |= courses  # same as all_courses = all_courses | courses
print("All courses with enrollment:", all_courses)

# 2. Courses ALL students share (intersection)
# Courses ALL students share (intersection)
list_courses = list(registrations.values())  
common_courses = list_courses[0]  
for courses in list_courses[1:]:
    common_courses &= courses  
print("Courses ALL students share:", common_courses)


alice_only = registrations["Alice"].copy()
for student, courses in registrations.items():
    if student != "Alice":
        alice_only -= courses
print("Courses ONLY Alice takes:", alice_only)


cs_students = set()
for student, courses in registrations.items():
    for course in courses:
        if course.startswith("CS"):
            cs_students.add(student)
            break
print("Students in CS courses:", cs_students)

print("\n")
print("== Part B: Prerequisite Check ===")

for student, courses in registrations.items():
    invalid_courses = {}
    for course in courses:
        missing = prerequisites[course] - courses
        if missing:
            invalid_courses[course] = missing
            if not invalid_courses:
                print(f"{student}: VALID")
    else:
        print(f"{student}: INVALID - Missing prerequisites:")
        for course, missing in invalid_courses.items():
            print(f"{course} requires {prerequisites[course]} but missing: {missing}")
        
print("\n")    
overload = {student for student, courses in registrations.items() if len(courses) >= 4}
print("Overloaded students (4+ courses):", overload)

math = {course for courses in registrations.values() for course in courses  if course.startswith("MATH")}
print("these are the math classes:", math)

identical = {(student1,student2) for studnet1, course1 in registrations.items() for student2, course2 in registrations.items() if studnet1 < student2 and course1 == course2}

if identical:
    print("The students with identical schdeuls:", identical)
    
else:
    print("The students with identical schedules: Not Found")
    
number_courses = {}
for courses in registrations.values():
    for course in courses:
        number_courses[course] = number_courses.get(course,0) + 1
        
        

for course, count in number_courses.items():
    print(f"{course}: {count} students")
    
    
under_enrolled = {course for course, count in number_courses.items() if count < 3}
print("The under enrolled courses (< 3students):", under_enrolled)


