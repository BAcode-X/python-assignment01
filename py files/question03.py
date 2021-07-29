# Question number 3

""" write an algorithm for the problem of determining prime number? """

# Naive method

def naive(n):
    is_prime = True

    # Iterate through the whole integers to find a divisor
    for i in range(2, n):
        # check divisibility
        if n % i == 0:
            is_prime = False
            break  # break out of the loop
    
    return is_prime

def dynamic_method(n):
    is_prime = True

    # Iterate till the number's square root
    for i in range(2, int(n**0.5)+1):
        # check divisibility
        if n % i == 0:
            is_prime = False
            break  # break out of the loop
    
    return is_prime

if __name__ == '__main__':
    n = 2
    
    # using naive method
    print(f"Determining if {n} is a prime or not using naive method ...")
    print(f"{n} is a prime number. \n" if naive(n) else f"{n} is not a prime number. \n")

    # using dynamic method
    print(f"Determining if {n} is a prime or not using dynamic method ...")
    print(f"{n} is a prime number." if dynamic_method(n) else f"{n} is not a prime number.")    