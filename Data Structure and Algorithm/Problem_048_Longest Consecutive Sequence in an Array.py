"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_Set = set()
        for num in nums:
            num_Set.add(num)

        longest = 0

        for num in num_Set:
            if num-1 not in num_Set:
                temp  = num
                count =1
                while temp + 1 in num_Set:
                    count +=1
                    temp +=1
                longest = max(longest , count)
        return longest

obj = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(obj.longestConsecutive(nums))
# Output 9