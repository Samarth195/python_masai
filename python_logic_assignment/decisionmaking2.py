age = int(input("Enter your age:"))
ID = input("Do you have an ID? (True/False):")
if age >= 18 and ID.lower() == "true":
    print("Entry Allowed.")
else:
    print("Entry Denied.")