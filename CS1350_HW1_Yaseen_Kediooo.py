contacts= {"Mom": 555_1234,"Dad": 555_5678, "Best Friends": 555_8888,"Pizza Place": 555_9999, "Work": 555_0000}

for person, number in contacts.items():
        print(f"{person} number is {number}")
        print(contacts["Mom"])
contacts["Dad"] = 555_4321

contacts["Dentist"] = 555_2222

print(contacts.get("Grandma","Contact not found"))

print(contacts)

del contacts["Pizza Place"]

print(contacts)

work_number = contacts.pop("Work")

print(f"Old Work number: {work_number}")

print(len(contacts))

print(f"Contacts: {contacts.keys()}")

print(f"Phone Numbers: {contacts.values()}")
