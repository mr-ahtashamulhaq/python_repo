"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1
        dic = {x:0 for x in range(len(nums)+1)}
        for num in nums:
            dic[num] =1
        for key in dic:
            if dic[key] == 0:
                return key
            
        # Method 2
        # n = len(nums)
        # return (((n*(n+1))//2) - sum(nums))
    
obj = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(obj.missingNumber(nums))
# Output : 8