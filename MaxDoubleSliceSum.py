'''Task description
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''

# https://app.codility.com/demo/results/trainingKFGKCJ-75U/
# Complexity O(N)

def solution(A):
    N = len(A)
    left_to_right = [0] * N
    right_to_left = left_to_right[:]
    max_sum = 0
    for i in range(1, N - 1): # Counting each sum of left part by Kadane
        max_sum = max(0, A[i] + max_sum)
        left_to_right[i] = max_sum
    max_sum = 0
    
    for i in range(N - 2, 0, -1): # Counting each of right part by Kadane
        max_sum = max(0, A[i] + max_sum)
        right_to_left[i] = max_sum

    # Now, having the both parts, it can be iterated, i + 1 is excluded due to
    # the task conditions
    answer = 0
    for i in range(0, N - 2):
        answer = max(answer, left_to_right[i] + right_to_left[i + 2])

    
    return answer


