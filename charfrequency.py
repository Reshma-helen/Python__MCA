str1=input("Enter a word:")
def char_frequency(str1):
    dict = {}
    for n in str1:
        key1 = dict.keys()
        if n in key1:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
char_frequency(str1)