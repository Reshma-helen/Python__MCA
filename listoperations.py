'''program to check length of two lists are same,sum of elements of two lists are same and print the 
same repeating values of two lists'''

list_1=[1,2,3,4,5]

list_2=[2,3,2,6,4]

if len(list_1)==len(list_2):
    print("Length of the two lists are equal \n")
else:
    print("Length of lists are not equal")
    
print("Sum of elements in list1 is:", sum(list_1))
print("Sum of elements in list2 is:", sum(list_2))

if sum(list_1)==sum(list_2):
    print("Sum of elements of two lists are equal")
    
else:
    print("Sum of elements are not equal \n\n") 
    
    
print("The repeating elements are:")

for i in list_1:
    if i in list_2:
        print(i)