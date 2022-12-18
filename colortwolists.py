color_list1=['red','yellow','green','black']
color_list2=['blue','red','yellow']

print("Color list1 is:",color_list1)
print("Color list2 is:",color_list2)

for i in color_list1:
    if i not in color_list2:
        print(i)