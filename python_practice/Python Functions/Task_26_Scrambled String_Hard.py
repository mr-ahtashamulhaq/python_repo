"""now same this with easiest explanation fiirst understand me what the problem exactly is then solve "Given two strings S1 and S2 of equal length, the task is to determine if S2 is a scrambled form of S1.

Scrambled string: Given string str, we can represent it as a binary tree by partitioning it into two non-empty substrings recursively.

 
To scramble the string, we may choose any non-leaf node and swap its two children. 
Suppose, we choose the node co and swap its two children, it produces a scrambled string ocder.
Similarly, if we continue to swap the children of nodes der and er, it produces a scrambled string ocred.

Note: Scrambled string is not the same as an Anagram.

Print "Yes" if S2 is a scrambled form of S1 otherwise print "No"."""


def isScramble(s1, s2):
    memo = {}

    def solve(a, b):
        if (a, b) in memo:
            return memo[(a, b)]

        if a == b:
            memo[(a, b)] = True
            return True

        if sorted(a) != sorted(b):
            memo[(a, b)] = False
            return False

        n = len(a)
        for i in range(1, n):
            if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                memo[(a, b)] = True
                return True


            if solve(a[:i], b[-i:]) and solve(a[i:], b[:-i]):
                memo[(a, b)] = True
                return True

        memo[(a, b)] = False
        return False

    return "Yes" if solve(s1, s2) else "No"

print(isScramble("great", "rgeat"))