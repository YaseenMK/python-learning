print("== Problem 1 ===")


def analyze_text(text):

    allowed_letters = " abcdefghijklmnopqrstuvwxyz "
    clean =""

    for random in text.lower():
        if random in allowed_letters:
            clean += random
            
    words = clean.split()

    word_counts = {}
    for w in words:
        word_counts[w] = word_counts.get(w, 0) + 1
    
    most_common = max(word_counts, key=word_counts.get)
    
    unique_count = sum(1 for w in word_counts if word_counts[w]== 1)
        
    return{
            "The word counts": word_counts,
            "Most common" : most_common,
            "The unique count" : unique_count
        }

        


sample = "The cat sat on the mat. The cat liked the mat!"
result = analyze_text(sample)
print(result["The word counts"])
print(result["Most common"])
print(result["The unique count"])

print("\n", "=== Problem 2 ===")
# 
class Roster:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = set()
        
    
    def enroll(self, name):
        self.students.add(name)
        
    def drop(self, name):   
        self.students.discard(name)
       
    
    def is_enrolled(self, name):
        return name in self.students
        
    
def common_students(roster1, roster2):
        return roster1.students & roster2.students 
       
        
        
    
    
def exclusive_students(roster1, roster2):
        return roster1.students ^ roster2.students

       
    
    
def print_report(rosters):
    for ro in rosters:
        print(f"{ro.course_name}: {len(ro.students)} students")
            
    common = rosters[0].students.copy()
    for ro in rosters[1:]:
            common &= ro.students
        
# Print each course and count
# Print students enrolled in ALL courses
# YOUR CODE HERE
   
    

cs101 = Roster("CS 101")
for name in ["Alice", "Bob", "Carol", "Dave"]:
    cs101.enroll(name)
       
cs201 = Roster("CS 201")
for name in ["Carol", "Dave", "Eve", "Frank"]:
    cs201.enroll(name)
    
cs301 = Roster("CS 301")
for name in ["Dave", "Eve", "Grace"]:
    cs301.enroll(name)
    
print(common_students(cs101, cs201))
# {'Carol', 'Dave'}
print(exclusive_students(cs101, cs201))
# {'Alice', 'Bob', 'Eve', 'Frank'}
print_report([cs101, cs201, cs301])
# CS 101: 4 students
# CS 201: 4 students
# CS 301: 3 students
# Enrolled in all courses: {'Dave'}



