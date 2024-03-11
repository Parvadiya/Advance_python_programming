# Write a Python class named rectangle constructed by a length and width and a method which will compute the area of a rectangle

class rectangle():  
    def __init__(self):
        self.length=""
        self.width=""
    
    def inputdata(self):   
        self.length=float(input("Enter Rectangle length : "))
        self.width=float(input("Enter Rectangle width : "))
        
    def showdata(self):    
        print(f"Rectangle length is :{self.length}")
        print(f"Rectangle width is :{self.width}")
        
    def find_area(self): 
        self.area=self.length*self.width
        print(f"area of a rectangle is {self.area:.2f}")

r1 = rectangle()  
r1.inputdata()   
r1.showdata()
r1.find_area()