"""Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero. Return true if such a triplet exists, otherwise, return false."""

class Solution:
    def longestConsecutive(self, arr):
        arr_set = set(arr)
        longest = 0
        
        for i in arr:
            if i - 1 not in arr_set:
                curr_long = 1
                current_element = i
                
                while current_element + 1 in arr_set:
                    current_element += 1
                    curr_long += 1
                    
                longest = max(longest, curr_long)
                
        return longest

obj = Solution()
arr = [2, 6, 1, 9, 4, 5, 3]
print(obj.longestConsecutive(arr))