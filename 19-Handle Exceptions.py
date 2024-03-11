# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

try:
    a=int(input("enter number :")) 
    print(10/0)
except ValueError:     
    print("not valid string")
except ZeroDivisionError:
    print("0 divisan is not allowed")
finally:        
      print("Python...")