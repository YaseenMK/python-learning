print("Exercise 1: Intermediate")
import re
text = """
Student grades: Alice-92, Bob-78, Charlie-85, Diana-95.
Room numbers: A101, B204, C310.
Emails: alice@school.edu, bob@school.edu.
"""
# 1: Find all names followed by scores (Name-Score)
name_scores = re.findall(r"(\w+)-(\d+)",text)
print(f"Scores: {name_scores}")

#2: Find all room numbers (letter + 3 digits)
rooms = re.findall(r"[A-Z]\d{3}",text)
print(f"Rooms: {rooms}")

#3: Find all email addresses
emails = re.findall(r"\w+@\w+\.\w+", text)
print(f"Emails: {emails}")

print("\n""Exercise 1: Advanced")
csv_lines = [
"Alice,Smith,25,Engineer,alice@corp.com",
"Bob,Jones,30,Designer,bob@corp.com",
"Carol,White,28,Manager,carol@corp.com",
]
for line in csv_lines:
    #  1: Use re.match with groups to extract all 5 fields
    # Pattern should match: word,word,digits,word,email
    match = re.match(r"(\w+),(\w+),(\d+),(\w+),(\w+@\w+\.\w+)",
        line
    )
    if match:
        first, last, age, role, email = match.groups()
        # TODO 2: Validate that age is between 18 and 65
        age_num = int(age)
        valid_age = 18 <= age_num <= 65
        
        #3: Print formatted output
        status = "✅" if valid_age else "⚠ age"
        print(f"{status} {first} {last} ({age}), {role}, {email}")
        
print("\n" "Exercise 2: Intermediate")
# Reformat phone numbers from various formats to (XXX) XXX-XXXX
phones = [
    "555-123-4567",
    "555.123.4567",
    "5551234567",
]
for phone in phones:
#1: First normalize — remove all non-digits
    digits = re.sub(r"\d+", "", phone)
#2: Use re.sub with groups to reformat
    formatted = re.sub(r"\d{3}(\d{3})(\d{4})", r"(\1)-\2-3", digits)
    print(f"{phone:<15} → {formatted}")


print("Exercise 2: Advanced")

text = "Python was created in 1991. Version 3.0 came in 2008. Now it's 2026."
#1: Use finditer to find all 4-digit years
# For each year, print the year and its context (10 chars before and after)
for match in re.finditer(r"\d{4}", text):
    print(f"Found '{match.group()}' at position {match.span()}")
    print(f" YEAR: {match.group()}")
    start, end = match.span()
    ctx_start = max(0, start - 10)
    ctx_end = min(len(text), end + 10)
    context = text[ctx_start:ctx_end]
    print(f"Context: {context}")
#Print the year, position, and context
#2: Use re.sub with a function to add 100 to every number in the text
def add_100(match):
    return str(int(match.group()) + 100)
result = re.sub(r"\d+", add_100, text)
print(f"\nAfter adding 100: {result}")


print("\n" "Exercise 3: Intermediate")
# : Rewrite this pattern using re.VERBOSE with comments
# Original: r"^(\d{2})/(\d{2})/(\d{4})$"
date_pattern = re.compile(r"^(\d{2})/(\d{2})/(\d{4})$"
    # : Add the pattern with comments explaining each part
    # Start of string
    # Two digits for month
    # Literal slash
    # Two digits for day
    # Literal slash
    # Four digits for year
    # End of string
,re.VERBOSE)

tests = ["03/15/2026", "3/15/2026", "03-15-2026", "12/25/2025"]
for t in tests:
    match = date_pattern.match(t)
    if match:
        print(f"✅ {t} → month={match.group(1)}, day={match.group(2)}, year={match.group(3)}")
    else:
        print(f"❌ {t}")
        
        
print("\n" "Exercise 3: Advanced")

class Validator:
    """
    Build a validation library with compiled patterns.
    Each method should return True/False.
    """
#1: Compile patterns as class attributes
    _email = re.compile(r"[\w.-]+@[\w.-]+\.\w+", re.IGNORECASE)
    _phone = re.compile(r"\d{3}[-.]?\d{3}[-.]?\d{4}")
    _zip = re.compile(r"^\d{5}(-\d{4})?$")  # Compile pattern for 5-digit ZIP, optional -XXXX
    _date = re.compile(r"\d{4}-\d{2}-\d{2}") # Compile pattern for YYYY-MM-DD
    @classmethod
    def is_email(cls, text):
        return cls._email.match(text) is not None
    
    @classmethod
    def is_phone(cls, text):
        return cls._phone.match(text) is not None
# 
    
    @classmethod
    def is_zip(cls, text):
        return cls._zip.match(text) is not None
    
    @classmethod
    def is_date(cls, text):
        return cls._date.match(text) is not None
# Test suite
tests = {
    "is_email": ["alice@example.com", "not-an-email", "bob@site.org"],
    "is_phone": ["555-123-4567", "5551234567", "55-123-4567"],
    "is_zip": ["46802", "46802-1234", "4680", "ABCDE"],
    "is_date": ["2026-03-15", "03/15/2026", "2026-13-01"],
}
for method_name, cases in tests.items():
    method = getattr(Validator, method_name)
    print(f"\n{method_name}:")
    
    for case in cases:
        result = method(case)
        icon = "✅" if result else "❌"
        print(f" {icon} {case}")
