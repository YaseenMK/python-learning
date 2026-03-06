import numpy as np

def grade_report(grades_2d):
    student_averages = np.mean(grades_2d, axis=1)



    assignment_averages= np.mean(grades_2d, axis=0)

    highest_student = np.argmax(student_averages)

    max_student_averages = np.max(student_averages)
    curved_grades = grades_2d * (100/ max_student_averages)

    passing = grades_2d >= 60
    
    return  {
        "student_averages": student_averages,
                "assignment_averages": assignment_averages,
                "highest_student": highest_student,
                "curved_grades":curved_grades,
                "passing": passing
        }




# Test cases
grades = np.array([
[85, 90, 78, 92], # Student 0
[70, 65, 80, 75], # Student 1
[95, 88, 92, 97], # Student 2
[60, 72, 68, 55] # Student 3
])

  
report = grade_report(grades)

print("Student averages:", report["student_averages"])
# [86.25 72.5 93. 63.75]
print("Assignment averages:", report["assignment_averages"])
# [77.5 78.75 79.5 79.75]
print("Highest student index:", report["highest_student"])
# 2
print("Curved grades (Student 0):", report["curved_grades"][0])
# [91.40 96.77 83.87 98.92] (approximately)
print("Passing (Student 3):", report["passing"][3])
# [ True True True False]