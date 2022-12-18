def factorial():
    fact=1
    n=int(input("Enter a value:"))
    for i in range(fact,n+1):
        fact=fact*i
    print("The factorial of ",n,"is",fact)
factorial()