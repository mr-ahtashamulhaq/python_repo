"""Given two Arrays A[] and B[] of length N and M respectively. Find the minimum number of insertions and deletions on the array A[], required to make both the arrays identical.
Note: Array B[] is sorted and all its elements are distinct, operations can be performed at any index not necessarily at end."""

class Solution:
    def minOperations(self, A, B):
        filtered_A = [x for x in A if x in B]
        
        i = j = 0
        common = 0
        while i < len(filtered_A) and j < len(B):
            if filtered_A[i] == B[j]:
                common += 1
                i += 1
                j += 1
            else:
                j += 1
        
        deletions = len(A) - common
        insertions = len(B) - common
        return deletions + insertions

A = [1, 2, 5, 3, 1]
B = [1, 3, 5]
sol = Solution()
print(sol.minOperations(A, B))