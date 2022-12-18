# program to print leap year between a range

s_year=int(input("Enter the starting year :"))
e_year=int(input("Enter the ending year :"))
print("The leap year from",s_year, "to",e_year, "are: ")
for i in range(s_year,e_year):
    if(i%4==0 and i%100!=0) or (i%400==0):
        print(i,end=" ")