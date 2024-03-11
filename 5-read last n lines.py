# Write a Python program to read last n lines of a file.

n=int(input("enter the number:")) 
fp=open("ex.txt","r")   
lines=fp.readlines()  
print(lines[-n:])  

fp.close()