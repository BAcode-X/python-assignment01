# Question number 9

""" Write a program to calculate the sum and average of a series of numbers. """

# a method to calculate average
def average(_sum, n):
    return _sum / n

if __name__ == '__main__':
    # accept input from the user
    num_series = list(map(int, input("Enter a series of numbers separated by a space.\n").split()))
    
    _sum = sum(num_series)

    _average = average(_sum, len(num_series))

    print("The sum of the numbers is %.0f and their average is %.2f." % (_sum, _average))