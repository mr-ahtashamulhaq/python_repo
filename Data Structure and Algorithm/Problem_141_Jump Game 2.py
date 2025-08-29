"""You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1."""
class Solution:
    def jump(self, nums):

        jump = 0
        left= 0
        right = 0
        n = len(nums)

        while right < (n-1):

            farthest = 0

            for i in range(left, right+1):
                farthest  = max(farthest, nums[i] +i)
            left = right+1
            right = farthest
            jump +=1
        return jump
        

obj =Solution()
print(obj.jump([2,3,1,1,4]))
# Output : 2