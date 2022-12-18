def list_even(l):
    l2=[]
    for i in l:
        if(i%2!=0):
            l2.append(i)
    return l2


n=input("Enter the values:")
list1=list(map(int,n.split()))
print("List before removing even integers: ",list1)

print("List after removing even integers:" )
list_even(list1)