# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

# -> A class in Python can be defined using the class keyword. As per the syntax above,
#   a class is defined using the class keyword followed by the class name and : operator after the class name,
#     which allows you to continue in the next indented line to define class members.
    
# -> What is SELF in Python? SELF represents the instance of class.
#   This handy keyword allows you to access variables, attributes, and methods of a defined class in Python.
#   The self parameter doesn't have to be named “self,” as you can call it by any other name.06

class student:  
    def __init__(self):  
        self.name=""
        self.lname=""
        self.M_no=""
    def getdata(self): 
#         name=""
#         lname=""
#         M_no=""
        
        self.name=input("enter name:")
        self.lname=input("enter lname:")
        self.M_no=int(input("enter M_no:"))
        
    def print_data(self): 
        print(f"name is :{self.name}\n lname is : {self.lname}\n M_No is : {self.M_no} ")
       

s1=student()  
s1.getdata()  
s1.print_data()