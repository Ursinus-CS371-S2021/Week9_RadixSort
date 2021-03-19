import numpy as np

def get_base10(x, place):
    """
    Return the digit at a particular place in a 
    base 10 number

    Parameters
    ----------
    x: int
        An integer
    place: int
        Which place to look at, where 0 is the 1s place,
        1 is the 10s place, 2 is the 100s place, etc
    """
    digit = 0
    s = "{}".format(x)
    if place < len(s):
        digit = int(s[-(1+place)])
    return digit

def radixsort(arr):
    """
    Sort an array using radix sort, assuming, for simplicity,
    that arr contains only nonnegative integers

    Parameters
    ----------
    arr: list

    """
    if len(arr) > 0:
        ## Find out the maximum number of digits needed to 
        ## represent a number in this array.  This will be
        ## the number of rounds in radix sort
        digits = 0
        for i in range(1, len(arr)):
            digits = max(digits, len("{}".format(arr[i])))

        for place in range(digits):
            staging = [0]*len(arr)
            counts = [0]*10

            ## TODO: Perform a count sort, but only using
            ## the digits at the place "place."  Based on
            ## the counts, move the elements in arr into the
            ## staging area list
            
            # Copy elements back
            for i in range(len(arr)):
                arr[i] = staging[i]
            print(arr)


np.random.seed(0)
arr = np.random.randint(0, 100, 20).tolist()
print(sorted(arr))
radixsort(arr)