# Question number 10

"""  Write an algorithm to read 100 numbers then display the largest. """

if __name__ == "__main__":
    # python can accept multiple integers on a single line 
    num_list = list(map(int, input("Enter a list of numbers separated by a space then press 'Enter'.\n").split()))

    num_list.sort() # sort the list in ascending order

    # display the last element in the list
    print(num_list[-1])