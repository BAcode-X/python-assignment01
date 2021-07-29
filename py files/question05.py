# Question number 5

""" Design an algorithm to convert a decimal number, n, to binary format """

def dec_to_bin(n):
    _bin = ''

    while n:
        _bin += str(n % 2)
        n = n // 2

    # reverse the value
    return _bin[::-1]

if __name__ == '__main__':
    n = int(input("Enter the number : "))
    
    print(f"The binary representation of {n} is {dec_to_bin(n)}")