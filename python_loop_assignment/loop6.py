num = 0
total = 0
while(True):
    num = int(input("Enter a number:"))
    total = num + total
    if(num == 0):
        break
    print(total)