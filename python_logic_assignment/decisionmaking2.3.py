bal = int(input("Enter the Account Balance:"))
amt = int(input("Enter the Amount to Withdraw:"))
ver = input("Enter the Verification Status (True/False):")
if bal >= amt and ver.lower() == "true":
    print("Withdrawal Successful.")
else:
    print("Withdrawal Failed.")