a=int(input("Enter first number:"))
b=int(input("Enter second number"))
def gcd(a,b):
    x,y,r=a,b,-1
    while(r!=0):
        r=a%b
        q=a//b
        print(a,"=",q,"*",b,"+",r)
        a,b=b,r
    print("GCD of x and y is:",a)
gcd(a,b)