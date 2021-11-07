def solution(A):
    N = len(A)
    if N < 3:
        return 0
    if N == 3:
        return 1

    possible_peaks = []
    for i in range(1, N - 1):
        if A[i] > max(A[i - 1], A[i + 1]):
            possible_peaks.append(i)
    if not possible_peaks:
        return 0

    M = len(possible_peaks)
    max_block_size = N
    while max_block_size % M != 0:
        max_block_size -= 1
    
    max_block_size = max_block_size // M
    
    if max_block_size == 1:
        return 1

    for block_size in range(max_block_size, 0, -1):
        remained_peaks = M
        start = block_size
        iterator = 0
        while iterator < M and remained_peaks:
            if possible_peaks[iterator] < start:
                remained_peaks -= 1
                iterator += 1
                if start == N:
                    return N // block_size
            else:

                start += block_size
    return 1
