def evenorodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number: "))
result = evenorodd(number)
print(f"The number {number} is {result}.")