def Merge(dict1, dict2):
    return(dict1.update(dict2))
 
 

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print("First dictionary is:",dict1)
print("Second dictionary is:",dict2)
 

Merge(dict1, dict2)
 
print("Merged dictionary is :",dict1)