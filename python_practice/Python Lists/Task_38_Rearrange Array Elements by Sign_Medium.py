"""Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order"""
class Solution:
    def rearrange(self, arr):
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        
        result = []
        i = j = 0

        while i < len(pos) or j < len(neg):
            if i < len(pos):
                result.append(pos[i])
                i += 1
            if j < len(neg):
                result.append(neg[j])
                j += 1
        
        return result

obj = Solution()
arr = [1, -2, 3, -4, 5, -6, -7, 8]
print(obj.rearrange(arr))