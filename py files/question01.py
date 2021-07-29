# Question number 1

""" write an algorithm to find the sum of first 100 natural numbers. """

# Naive method

def naive(n):
    _sum = 0

    for i in range(n+1):
        _sum += i
    
    return _sum

# Dynamic method

def dynamic_method(n):
    _sum = (n * (n + 1)) // 2

    return _sum

if __name__ == '__main__':
    n = 100

    print(f"Sum of the first {n} natural numbers using naive method is {naive(n)}")

    print(f"Sum of the first {n} natural numbers using dynamic method is {dynamic_method(n)}")