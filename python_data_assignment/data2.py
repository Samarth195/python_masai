dict1={
    "Ravi": "1234567890",
    "Suresh": "0987654321",
    "Ramesh": "1122334455",
}
print("All Contacts :")
for name, number in dict1.items():
    print(f"{name}: {number}")
name_to_search = input("Enter a name to search for their contact number:")
if name_to_search in dict1:
    print(f"Contact number of {name_to_search} is: {dict1[name_to_search]}")
else:
    print(f"{name_to_search} not found in contacts.")
