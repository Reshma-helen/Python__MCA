# A few lambda functions to calculate area  of common geometric figures

ln=int(input("Enter the length of the rectangle: "))
bh=int(input("Enter the breadth of the rectangle: "))

re_area = lambda ln, bh : ln*bh
print("Area of Rectangle is: ", re_area(ln,bh),"\n")

b=int(input("Enter the base of the triangle: "))
h=int(input("Enter the height of the triangle: "))

tr_area = lambda b,h:(b*h)/2
print("Area of Triangle  is: ", tr_area(b,h),"\n")

s=int(input("Enter the side of the square: "))

sq_area=lambda s: s*s
print("Area of Square is:", sq_area(s),"\n")