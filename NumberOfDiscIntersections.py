'''Task description
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].'''

# https://app.codility.com/demo/results/trainingYCCPRN-XU6/
#O(N*log(N)) or O(N)


def solution(A):
    N = len(A)
    if N < 2:
        return 0
    disks_start = [0] * len(A) # left point of each circle
    disks_end = [0] * len(A) # right point of each circle
    disks_count = 0
    intersects = 0
    
    for i in range(N):
        disks_start[i] = i - A[i]
        disks_end[i] = i + A[i]

    disks_start.sort()
    disks_end.sort()
    start_counter = 0
    end_counter = 0

    while start_counter < len(disks_start):
        if disks_start[start_counter] <= disks_end[end_counter]: # don't forget about 0 radius cases
            intersects += disks_count
            disks_count += 1
            start_counter += 1
        else:
            disks_count -= 1
            end_counter += 1
        if intersects > 1e7:
            return -1
    return intersects
