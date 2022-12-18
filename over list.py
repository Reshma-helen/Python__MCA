lst=[]
n=int(input ("enter how many values to be inserted on alist:"))
for i in range(0,n):
    value=int(input("enter a value:"))
    if value>=100:
        lst.append('over')
    else:
        lst.append(value)
print("the given list after modification while inserting :",lst)