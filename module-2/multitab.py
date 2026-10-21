#------------------------------------------------------------------------------
# This module defines multitab() a multiplication table generator.
#------------------------------------------------------------------------------
import math

def multitab(n):
    """Print multiplication table up to n.

    Parameters
    ----------
    n : positive integer scalar

    Returns
    -------
    None
    """
    assert (type(n) is int) and (n > 0), "n must be positive integer"

    ### THIS IS WHERE YOU COME IN
    ### USE AS MANY LINES AS YOU NEED
    ### USE A FOR LOOP OR WHILE LOOP, WHICHEVER YOU LIKE
    ### YOU WILL PROBABLY NEED TO LOOK UP SOME THINGS
    ### YOU WILL DISCOVER A USEFUL OPTIONAL PARAMETER TO THE FUNCTION PRINT()
    print(" ", end = " ") # align the first row
    for i in range(1, n + 1): # for loop that prints 1 through n for row
        print(f"\033[4m{i}\033[0m", end = " ") # using the underline property of print function
    print("\n") # starting new line for actual table
    for i in range(1, n + 1):
        print(f"\033[4m{i}\033[0m", end = " ") # print the column indicators 1 through n underlined
        for k in range(1, n + 1):
            print(i * k, end = " ") # print the products on same line with space
        print("\n") # start new line afterwards
    return None

### To run as a utility
if __name__ == '__main__':
    n = int(input("Multiplication table size: "))
    multitab(n)
