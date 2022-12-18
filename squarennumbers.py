#program to print square of n numbers

num=int(input("Enter the range :"))
list_1=[i**2 for i in range(1,num+1)]
print("Square of ",num," numbers in a list using list comprehension :",list_1)