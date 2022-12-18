n=int(input("Enter the number:"))
def factors(n):
    print("The factors of",n,"are:")
    for i in range(1,n+1):
        if n % i==0:
            print(i,end="  ")
factors(n)