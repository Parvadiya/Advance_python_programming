# Write a Python program to copy the contents of a file to another file.

fp=open("ex.txt","r")
fp1=open("ex1.txt","w")
for line in fp:
    fp1.write(line)
fp1.close()
fp1=open("ex1.txt","r")
print(fp1.read())