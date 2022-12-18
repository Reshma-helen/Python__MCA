n=int(input("Enter number of terms:"))
a=0
b=1
print("Fibonacci series of firt n terms is:")
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c