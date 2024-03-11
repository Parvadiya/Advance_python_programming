# Write a Python program to count the frequency of words in a file

file = open("ex.txt","r")
n = ' '.join(line for line in file.read().splitlines())
n = n.split(' ')
dict= {}
for word in n:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
print(dict)        
file.close()