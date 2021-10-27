#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

def add(num1,num2):
    print( str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))

def sub():
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))

def main ():
     while True :
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input()
        if calc1 == "Q":
            break
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input()
        if calc2 == "q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()
        if operation == "+":
            add(calc1,calc2)
        elif  operation == '-':
            sub(calc1,calc2)
        else:
            print("\n Not a valid entry. Restarting...")

def add(num1,num2):
    print( str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    
def sub():
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    
main()
