# Write a Python program to write a list to a file.

items = ["yash","raj","savan","om"]
file = open('11.txt','w')
file.writelines(items)
file.close()