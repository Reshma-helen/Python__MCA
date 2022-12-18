n = int(input("Enter the number of rows: "))  
def pattern(n):
    for i in range(1,n+1): 
        print()
        for j in range(1, i + 1):   

            print(j*i, end=" ")  
pattern(n) 