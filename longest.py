a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element:" )
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>=max1): 
        max1=len(i)
        temp=i
        if len(temp)==max1:
            print("The word with the longest length is:",temp ,"and the length is:",max1)