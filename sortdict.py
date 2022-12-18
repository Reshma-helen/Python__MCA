d1={9:'nine',5:'five',10:'ten',2:'two',8:'eight'}
print("The dictionary is: \n",d1)
l1=list(d1.items())
l1.sort()
d1=dict(l1)

print(" \n Dictionary in ascending order is: \n ",d1)

l2=list(d1.items())
l2.sort(reverse=True)
d2=dict(l2)

print(" \n  Dictionary in descending order is: \n",d2)