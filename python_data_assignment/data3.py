employee = (123,"Sam","IT")
roles = {"admin","editor","viewer"}
print(f"Employee Details: ID={employee[0]}, Name={employee[1]}, Department={employee[2]}")
if "admin" in roles:
    print("Admin Access : Yes")
else:
    print("Admin Access : No")