# Question number 4

""" write an algorithm which generates first 50 items of the Fibonacci series:  1, 1, 2, 3, 5, 8, """

# dynamic method

def fibonacci(n):
    fib_list = [0 for i in range(n)]  # create a list with 50 elements which are 0
    
    # initialize fibonacci of 0 and 1
    fib_list[0], fib_list[1] = 1, 1

    # start the iteration from 2
    for i in range(2, n):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    
    return [str(i) for i in fib_list]


if __name__ == '__main__':
    n = 50

    print("The first 50 elements of the Fibonacci series")
    print(", ".join(fibonacci(n)))