print("===Exercise 1===")


def clean_contact():
    name = " jOhN sMiTh "
    email = " JOHN@Email.COM "
    phone = " 555-123-4567 "
  

    # 1: Strip whitespace from name, then title-case it
    clean_name = name.strip().title()
    
    
    

    #  2: Strip whitespace from email, then lowercase it
    clean_email = email.strip().lower()
   
    
    

    # 3: Strip whitespace from phone
    clean_phone = phone.strip()


    print(f"Name: {clean_name}") # Expected: "John Smith"
    print(f"Email: {clean_email}") # Expected: "john@email.com"
    print(f"Phone: {clean_phone}") # Expected: "555-123-4567"
clean_contact()
    
    
print("\n")
print("===Exercise 2===")
students = [
("Alice", 92.5, "A"),
("Bob", 78.3, "C+"),
("Charlie", 85.7, "B"),
]
# Print a formatted table


# Header: Name (left 12), Score (right 8, 1 decimal), Grade (right 6)
print(f"{'Name':<12}{'Score':>8}{'Grade':>6}")


print("-" * 26)
for name, score, grade in students:
    print(f"{name:<12}{score:>8.1f}{grade:>6}")
#  print each row with proper alignment

#  Calculate and print average score with 2 decimal places
total = 0

for name, score, grade in students:
    total += score
    
    average = total / len(students)
    
    print(f"\nAverage Score: {average:.2f}")
    
print("\n")
print("===Exercise 3===")
import re

text = "My student ID is s12345 and my room is B204"

# Use re.search to find a single digit anywhere in the text
match =  re.search(r'\d',text)
if match:
    print(f"First digit: {match.group()}")
    print(f"Found at position: {match.start()}")
# Search for an uppercase letter followed by a digit (like B2)


match2 = re.search(r"[A-Z]\d", text)
if match2:
    print(f"Letter-digit pair: {match2.group()}")
    print(f"Span: {match2.span()}")
# Search for "s" followed by exactly 5 digits (the student ID)

match3 = re.search(r"s\d{5}", text)
if match3:
    print(f"Student ID: {match3.group()}")