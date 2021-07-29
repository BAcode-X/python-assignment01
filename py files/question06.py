# Question number 6

""" 
Write an algorithm that  will calculate the roots of a quadratic equation.

    quadratic equation => ax^2 + bx + c = 0

"""

from math import sqrt

def eval_quadratic(a, b, c):
    # evaluate the root value
    if b**2 - (4 * a * c) < 0 or a == 0:
        return None
    else:
        d = sqrt(b**2 - (4 * a * c))

    ans01 = (-b + d) / (2 * a)  # answer number 1

    ans02 = (-b - d) / (2 * a)  # answer number 2
    
    return ans01, ans02

if __name__ == '__main__':
    # accept input from the user
    a, b, c = map(int, input("Enter a, b and c separated by a space then press 'Enter'\n").split())

    ans = eval_quadratic(a, b, c)

    print(f"The values of x1 and x2 are : {ans[0], ans[1]}" if ans else "The quadratic equation has no answer")