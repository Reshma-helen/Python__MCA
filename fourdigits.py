#program to generate a list of four digit numbers in a given
# range will all their digits even and the number is a perfect square



a=[]
b=int(input("Enter the starting range:"))
c=int(input("Enter the ending range:"))
for i in range(b,c+1):
    d=i*i
    d1=d
    while d1>0:
        digit=d1%10
        if (digit%2)==0:
            d1=d1//10
            if d1==0:
                a.append(d)
        else:
                break
print(a)