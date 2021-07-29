# Question number 2

""" write an algorithm to find the largest of three numbers x, y and z. """

# A method to find the largest number out of 3 numbers

def largest_number(x, y, z):
    # put the numbers in a list
    temp = [x, y, z]

    # sort the list in ascending order
    temp.sort()

    # pick the last element
    return temp[-1]

if __name__ == '__main__':
    x, y, z = map(int, input("Enter the value of x y and z separated by a space then press 'Enter'\n").split())

    answer = largest_number(x, y, z)

    print(f"The largest number is {answer}")