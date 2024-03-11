# Write python program that user to enter only odd numbers, else will raise an exception.

try:
    num=int(input("Enter number:"))
    if num%2==0:
        print(f"try block execute \n {num} is Even number")
except ValueError:
        print(" Not string..only int num allowed")      