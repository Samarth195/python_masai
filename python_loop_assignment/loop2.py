ag = "admin123"
while True:
    user_input = input("Enter the password:")
    if user_input == ag:
        print("Access Granted.")
        break
    else:
        print("Access Denied. Try Again.")
