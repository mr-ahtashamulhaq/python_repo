"""You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer."""

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        posind= 0
        negind = 1
        for num in nums:
            if num>= 0:
                result[posind] = num
                posind +=2
            else:
                result [negind] = num
                negind +=2
        return result

obj = Solution()
nums = [3,1,-2,-5,2,-4]
print(obj.rearrangeArray(nums))
# Output : [3, -2, 1, -5, 2, -4]        