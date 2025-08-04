"""maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position."""

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 0
        i = 0
        
        while i < n:
            if i >= n - 1:
                return jumps
            
            
            maxReach = i + arr[i]
            
            if maxReach >= n - 1:
                return jumps + 1
            
            
            best = i + 1
            for j in range(i + 1, maxReach + 1):
                if j + arr[j] > best + arr[best]:
                    best = j
            
            if best == i:
                return -1  
            
            i = best
            jumps += 1
        
        return -1

obj = Solution()
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(obj.minJumps(arr))