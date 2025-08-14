"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i= 0
        n = len(nums)
        total = 0
        temp = 0
        while i<n:
            if nums[i] == 1:
                temp +=1
            else:
                total = max(temp , total)
                temp = 0
            i +=1
        return max(total,temp)

obj = Solution()
nums = [1,1,0,1,1,1]
print(obj.findMaxConsecutiveOnes(nums))
# Output : 3