import numpy as np

def countsort(arr):
    """
    Sort an array using count sort, assuming, for simplicity,
    that arr contains only nonnegative integers

    Parameters
    ----------
    arr: list

    """
    if len(arr) > 0:
        ## Step 1: Find the maximum element of the array
        max_elem = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_elem:
                max_elem = arr[i]
        
        ## Step 2: Create an array of length max_elem+1 and 
        ## store the counts at each element
        counts = [0]*(max_elem+1)
        for x in arr:
            counts[x] += 1
        
        ## Step 3: Loop through the counts array and put elements
        ## at their appropriate place 
        idx = 0
        for x, count in enumerate(counts):
            for k in range(count):
                arr[idx] = x
                idx += 1

np.random.seed(0)
arr = np.random.randint(0, 100, 20).tolist()
print(sorted(arr))
countsort(arr)
print(arr)