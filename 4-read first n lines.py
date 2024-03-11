# Write a Python program to read first n lines of a file.

n=int(input("enter the number:"))    
fp=open("ex.txt","r")  
for i in range(0,n):      
    print(fp.readline())  
    print("---------------")
fp.close()