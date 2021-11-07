'''Task description
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P and Q is an integer within the range [1..N];
P[i] ≤ Q[i].'''
# https://app.codility.com/demo/results/trainingHAKHQH-3YS/
# Complexity: O(N * log(log(N)) + M)

def solution(N, P, Q):
    F = [0] * (N + 1)
    i = 2
    while i * i <= N:
        if F[i] == 0:
            k = i * i
            while k <= N:
                if F[k] ==0:
                    F[k] = i
                k += i
        i += 1

    semi_primes = [0] * (N + 1)
    for k in range(1, N + 1):
        if F[k] > 0 and F[k // F[k]] == 0:
            semi_primes[k] = 1
    
    semi_primes_prefix = [0] * (N + 2)
    for i in range(1, N + 2):
        semi_primes_prefix[i] = semi_primes_prefix[i - 1] + semi_primes[i - 1]

    max_len = len(P)
    ans = []
    for i in range(max_len):
        ans.append(semi_primes_prefix[Q[i] + 1] - semi_primes_prefix[P[i]])
    
    return ans
