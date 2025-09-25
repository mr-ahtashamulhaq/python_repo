"""You are given an array of integers arr[], return the Longest Increasing Subsequence (LIS) of the given array.
LIS is the longest subsequence where each element is strictly greater than the previous one.
Note: If multiple LIS of the same maximum length exist, return the one that appears first based on the lexicographical order of their indices (i.e., the earliest combination of positions from the original sequence)."""
class Solution:
    #TC --> O(N^2)
    
    #Modification in Algorithmic approach
    def getLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        parent = [i for i in range(n)]

        last_ind = 0  # index where LIS ends

        for index in range(n):
            for prev in range(index):
                if nums[prev] < nums[index]:    #Can we take it ?
                    if dp[index] < 1 + dp[prev]: # if this LIS length is greater than already stored length 
                        
                        dp[index] = 1 + dp[prev] # then update it 
                        parent[index] = prev    #update its parent

            if dp[index] > dp[last_ind]:
                last_ind = index


        result = []
        i = last_ind
        
        while parent[i] != i:
            result.append(nums[i])
            i = parent[i]
            
        result.append(nums[i])

        result.reverse()
        return result


obj = Solution()
nums = [10,9,2,5,3,7,101,18]
print(obj.getLIS(nums))

# Output : [2, 5, 7, 101]