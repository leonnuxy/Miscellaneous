# Given an array A of N integers, 
# the function returns the smallest 
# positive integer (greater than 0) 
# that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], 
# the function should return 5.

# Given A = [1, 2, 3], the function should return 4.
# Given A = [-1, -3], the function should return 1.
# Efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer 
# within the range [-1,000,000..1,000,000].

def solution(A):

    A.sort()
    m = max(A)

    if m < 1:
       return 1

    
    A = set(A)
    B = set(range(1, m + 1))
    D = B - A

    if len(D) == 0:
        return m + 1
    else:
        return min(D)
