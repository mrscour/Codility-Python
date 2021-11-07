'''Task description
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].'''
# https://app.codility.com/demo/results/training982QC5-EK8/
# Complexity: O(N * log(N))

from math import sqrt
def solution(A):
    count_dict = {}
    N = len(A)
    for i in A:
        count_dict[i] = count_dict.setdefault(i, 0) + 1
    counted = {}

    for i in count_dict:
        divisors = 0
        for k in range(1, int(sqrt(i)) + 1):
            if i % k == 0:
                divisors += count_dict.get(k, 0)
                if i // k != k:
                    divisors += count_dict.get(i//k, 0)
        counted[i] = N - divisors
    
    return [counted[i] for i in A]
