n=input("enter elements:")
list1=list(map(int,n.split()))
print(list1)
total=0
for i in range(0,len(list1)):
        total=total+list1[i]
print("sum of all items in the list is:",total)