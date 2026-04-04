print("Exercise 1: Intermediate")

import re
dates = ["03-15-2026", "12-25-2025", "01-01-2000"]
for date in dates:
    #1: Write a pattern with named groups for month, day, year
    pattern = r"(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})"
    match = re.search(pattern, date)
    # Format: MM-DD-YYYY
if match:
#2: Extract using named groups

    info = match.groupdict()
    print(f"{info['month']}/{info['day']}/{info['year']}")
    
print("\n" "Advanced:")

log_entries = [
    "[2026-03-10 14:30:45] Server started",
    "[2026-03-10 09:15:02] User login",
    "[2026-03-11 22:00:00] Backup complete",
]
pattern = r"\[(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})\] (?P<message>.+)"

for entry in log_entries:
    #: Write a pattern that captures date, time, and message
    match = re.search(pattern, entry)
    if match:
        print(f"Date: {match.group('date')}, Time: {match.group('time')}, Message: {match.group('message')}")
    # The bracket section: [YYYY-MM-DD HH:MM:SS]
    # Then the message after "] "
    # Use named groups: date, time, message


print("Exercise 2: Intermediate:")

sentences = [
    "This is is a problem",
    "The the cat sat down",
    "No duplicates here",
    "I really really like Python",
]
for sentence in sentences:
# Use a backreference to find repeated words

# Pattern: word boundary, capture a word, whitespace, same word, word boundary
    match = re.search(r"\b(\w+)\s+\1\b", sentence)
    
    if match:
        print(f"Duplicate '{match.group(1)}' in: {sentence}")
    else:
        print(f"No duplicates in: {sentence}")
        
print("\n" "Advanced:")

records = [
"Name: Alice Smith | ID: EMP-001 | Dept: Engineering",
"Name: Bob Jones | ID: EMP-042 | Dept: Marketing",
"Name: Carol White | ID: EMP-108 | Dept: Sales", ]

pattern = r"Name:\s*(?P<name>.+?) \| ID: (?P<id>EMP-\d{3}) \| Dept: (?P<dept>.+)"

for record in records:
    match = re.search(pattern, record)
    if match:
        d = match.groupdict()
        # 1: Print each field using the dict
        print("Name:", d["name"])
        print("ID:", d["id"])
        print("Dept:", d["dept"])
        # 2: Print the position of the ID field using match.span('id')
        
        
        id_span = match.span("id")
        print(f"ID Location -->: {id_span}")
        pass

print("\n" "Exercise 3: Intermediate")

files = [
    "report.pdf", "photo.jpg", "data.csv",
    "script.py", "style.css", "page.html",
    "notes.txt", "image.png", "app.js"
]

for f in files:
    lower_f = f.lower()
    #1: Match document extensions (.pdf, .doc, .txt, .csv)
    is_doc = re.search(r"\.(pdf|doc|txt|csv)$",lower_f)# Write your pattern
    
    #2: Match image extensions (.jpg, .jpeg, .png, .gif)
    is_img = re.search(r"\.(jpg|jpeg|png|gif)$",lower_f ) # Write your pattern
    
    #3: Match code extensions (.py, .js, .html, .css)
    is_code = re.search(r"\.(py|js|html|css)$",lower_f ) # Write your pattern
    
    if is_doc:
        category = f"Document ({is_doc.group(1)})"
    elif is_img:
        category = f"Image ({is_img.group(1)})"
    elif is_code:
        category = f"Code ({is_code.group(1)})"
    else:
        category = "Other"
    print(f"{f:<15} → {category}")
    
print("\n" "Advanced:")

dates = [
    "2026-03-15", # ISO: YYYY-MM-DD
    "03/15/2026", # US: MM/DD/YYYY
    "15 Mar 2026", # Text: DD Mon YYYY
    "March 15, 2026", # Long: Month DD, YYYY
    "not a date",
]

for date in dates:
    #1: Try ISO format with named groups
    iso = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date)
    
    #2: Try US format
    us = re.search(r"(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})", date)
    #3: Try text format (3-letter month abbreviation)
    
    text_fmt = re.search(r"(?P<day>\d{1,2}) (?P<month>[A-Za-z]{3}) (?P<year>\d{4})", date)
    #4: Try long format — write the pattern yourself
    long_fmt = re.search(r"(?P<month>[A-Za-z]+) (?P<day>\d{1,2}), (?P<year>\d{4})", date)
 # Match "March 15, 2026" with named groups
    matched = iso or us or text_fmt or long_fmt
    if matched:
        d = matched.groupdict()
        print(f"'{date}' → month={d['month']}, day={d['day']}, year={d['year']}")
    else:
        print(f"'{date}' → no match")
        
        
print("\n" "Exercise 2: Beginner")

text = "The cat sat on the mat near the bat"
#  1: Replace all 3-letter words ending in "at" with "___"
result = re.sub(r"\b\wat\b", "___", text)
print(result)
#  2: Replace only the first occurrence
result2 = re.sub(r"\b\wat\b", "___", text, count=1)
print(result2)