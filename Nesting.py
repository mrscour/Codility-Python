'''Task description
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")"'''
# Complexity O(N)
# https://app.codility.com/demo/results/trainingHTHSY3-ZEN/
# If our selector goes < 0, it's mean it was opened with ")"

def solution(S):
    selector = 0
    for i in S:
        if i == "(":
            selector += 1
        else:
            selector -= 1
        if selector < 0:
            return 0
    return 1 if selector == 0 else 0 # lastly checking if all parent "(" are closed
