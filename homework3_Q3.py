import numpy as np 

# Student scores: 6 students, 4 exams
scores = np.array([[85, 90, 78, 92], # Alice
    [70, 65, 72, 68], # Bob
    [95, 98, 94, 97], # Carol
    [60, 55, 58, 62], # Dave
    [88, 85, 90, 87], # Eve
    [75, 80, 77, 82]  # Frank
])

students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']

exams = ['Exam1', 'Exam2', 'Exam3', 'Exam4']

print("Carol Exam 2 score:", scores[2,1])

print("Alice scores are:", scores[0])

print("All of the Exam 3 score:", scores[:,2])

print(scores[1:3, 0:2])


        
print(scores >= 90)

over_90 = scores >= 90

print(scores[over_90])

print(scores[over_90].size)
        
    
average = scores.mean(axis=1)

about_85= average >= 85

print(about_85)

for person in range(len(students)): 
    if about_85[person]:
        print(students[person])
        
minimum = scores < 60

scores[minimum] = 60

print(scores)
