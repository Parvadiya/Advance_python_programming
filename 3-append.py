# Write a Python program to append text to a file and display the text.

fp=open("ex.txt","a") 
fp.write("mo.:8238391024\n") 
# print(fp.write)
fp.close()   
fp=open("ex.txt","r")
print(fp.read()) 
fp.close()