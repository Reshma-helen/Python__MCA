#input a string and replace all the occurrence of the first letter in '$''


word1=input("enter any word:")
char=word1[0]
word=word1.replace(char,'$')
word=char+word[1:]

print("Before replacement:" ,word1)
print("after replacement:", word)