list1=[]
for i in range(0,8):
    num=int(input("Enter a number:"))
    list1.append(num)
print(f"Full List :{list1}")
print(f"First 3 Elements :{list1[0:3]}")
print(f"Last 3 Elements :{list1[-1:-4:-1]}")
print(f"Maximum Element :{max(list1)}")
print(f"Minimum Element :{min(list1)}")
print(f"Average of the List :{sum(list1)/len(list1)}")