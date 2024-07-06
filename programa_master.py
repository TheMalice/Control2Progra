from function1 import justify
from function2 import function2
from function3 import CRUD

def programa_master():
    print("Hello, welcome to the master program for the 2nd Test of Programación Avanzada \n Please choose the function you want to run:")
    print("1) 'function1.py' that justifies a given string/text. \n 2) 'function2.py' that executes various DP problems in a given text file. \n 3) 'function3.py' that executes CRUD operations in a given text file.")
    print("Enter a number below:")
    chosen_one = int(input())
    if not chosen_one:
        return f"Please enter a number between 1 and 3."
    elif chosen_one == 1:
        print("You have chosen the program 1 'Justify':")
        print("Please write some text to justify down below:")
        text = input()
        print("Now, indicate the maximum line width for the text:")
        line_width = int(input())
        print(justify(text, line_width))
    
    elif chosen_one == 2:
        print("You have chosen the program 2 'DP problems':")
        function2()
    
    else:
        print("You have chosen the program 3 'CRUD operations':")
        CRUD()


if __name__ == "__main__":
    programa_master()

