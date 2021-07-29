# Question number 8

""" 
Write a program that accepts an input of an examination mark and test it for the award of a grade.

The titles are:
    >= 80 Distinction 
  	>= 60 Merit 
  	>= 40 Pass 
 	< 40 fail
"""

# evaluater method
def award(mark):
    if mark > 100 or mark < 0:
        return "Invalid mark input."
    if mark >= 80:
        return "Distinction"
    elif mark >= 60:
        return "Merit"
    elif mark >= 40:
        return "Pass"
    else:
        return "Fail"

if __name__ == '__main__':
    # start an infinite loop
    while 1:

        cmd = input("Enter the grade of a student or type 'exit' to quite the program then press 'Enter'.\n")

        if cmd == "exit":
            break
        else:
            print(award(int(cmd)))